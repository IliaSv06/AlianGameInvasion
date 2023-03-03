import pygame
import sys

import alien
from bullet import Bullet
from alien import Alien
from time import sleep
from anime import Explosion

def key_left_right_downn(event, ship):
        '''Переместить корабль вправо/влево при задержки кнопки'''
        if event.key==pygame.K_RIGHT:
            ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            ship.moving_left=True

def key_left_right_up(event, ship):
    '''Отпуск левой/правой кнопки'''
    if event.key==pygame.K_RIGHT:
                ship.moving_right=False
            
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

def top_buttom_keydown(ship, event):
    '''Проверка верней/нижней кнопки при зажатии'''
    if event.key==pygame.K_UP:
            ship.moving_top=True
    if event.key==pygame.K_DOWN:
            ship.moving_bottom=True

def top_buttom_keyup(ship, event):
    '''Отпуск верхней/нижней кнопки'''
    if event.key==pygame.K_UP:
            ship.moving_top=False
    if event.key==pygame.K_DOWN:
            ship.moving_bottom=False

def fire_bullets_down(ship, event, bullets, ai_setting, screen, sound1):
    '''Отвечает за стрельбу'''
    if event.key==pygame.K_SPACE:
            ai_setting.flag_fire = True

def fire_bullets(ship, bullets, ai_setting, screen, sound1, stats):
    if ai_setting.flag_fire:
        now_time = pygame.time.get_ticks()
        second_time = (now_time - stats.first_time)/1000
        if second_time > 0.3:
            stats.first_time = now_time
            new_bullet = Bullet(ai_setting, screen, ship)
            bullets.add(new_bullet)
            sound1.play()

def fire_bullet_up(ai_setting, event):
    if event.key == pygame.K_SPACE:
        ai_setting.flag_fire = False

def check_keydown_events(ship, event, bullets, ai_setting, screen, sound1, play_button, stats, aliens, score):
     if event.type==pygame.KEYDOWN:
            '''Задержка кнопки'''
            if event.key==pygame.K_q:
                sys.exit()
            if event.key==pygame.K_SPACE and not stats.game_active:
                restart(stats, aliens, ship, screen, bullets, ai_setting, score)
            key_left_right_downn(event, ship)
            top_buttom_keydown(ship, event)
            fire_bullets_down(ship, event, bullets, ai_setting, screen, sound1)
           
def check_keyup_events(ship, event, ai_setting):
    if event.type==pygame.KEYUP:
        '''Отпуск кнопки'''
        key_left_right_up(event, ship)
        top_buttom_keyup(ship, event)
        fire_bullet_up(ai_setting, event)

def check_events(ship, bullets, ai_setting, screen, play_button, stats, aliens, score, sound1):
    '''Цикл событий'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button, stats, mouse_x, mouse_y, aliens, ship, screen, bullets, ai_setting, score)
        if event.type == pygame.USEREVENT and stats.game_active:
            create_fleet(screen, stats, aliens, ai_setting)

        check_keydown_events(ship, event, bullets, ai_setting, screen, sound1, play_button, stats,  aliens, score)
        check_keyup_events(ship, event, ai_setting)

def check_play_button(play_button, stats, mouse_x, mouse_y, aliens, ship, screen, bullets, ai_setting, score):
    '''Событие при нажатии на кнопку "Play"'''
    button_clicked=play_button.rect.collidepoint(mouse_x, mouse_y) #обнаружаются коллизии между кнопкий и точкой клика
    if button_clicked and not stats.game_active:
        restart(stats, aliens, ship, screen, bullets, ai_setting, score)

def restart(stats, aliens, ship, screen, bullets, ai_setting, score):
        pygame.mouse.set_visible(False) #скрытие указателя мыши на экране
        ai_setting.initialize_dynamic_settings() # сброс параметров скорости
        #Сброс игровой статистики
        stats.reset_stats()
        score.prep_score()
        score.make_level()
        stats.game_active=True
        #Очитска мусора в экране
        bullets.empty()
        aliens.empty()
        #Создание нового флота пришельцев
        score.make_ships()
        ship.center_ship()
        pygame.mixer.music.load('music/rick_and_morty_theme.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

def update_screen(ship, screen, ai_setting, bullets, aliens, play_button, stats, score, animation_object, sound1):
    '''Проресовка экрана''' 
    screen.fill(ai_setting.bg_color)
    screen.blit(ai_setting.background, ai_setting.background_rect)
    score.draw_score()
    ship.blitme()
    aliens.draw(screen)
    animation_object.update()
    animation_object.draw(screen)
    fire_bullets(ship, bullets, ai_setting, screen, sound1, stats)
    if not stats.game_active:
        play_button.draw_button()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()

def update_bullets(bullets, aliens, ai_setting, screen, ship, score, stats, animation_object):
    '''Управление пулями (удаление)'''
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
        new_flot_and_collisions(bullets, aliens, screen, ai_setting, ship, score, stats, animation_object)

def new_flot_and_collisions(bullets, aliens, screen, ai_setting, ship, score, stats, animation_object):
    '''Удаление пуль и пришельцев в коллизии и создание повторного флота'''
    collisions=pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for alien_sprite in collisions.values():
            for alien in alien_sprite:
                boom = Explosion(alien.rect.center)
                animation_object.add(boom)
                ai_setting.sound_boom.play()
                stats.score+=ai_setting.alien_point * len(alien_sprite)
                score.prep_score()
                check_high_score(stats, score)

    if stats.limit_object <=0 and len(aliens)==0:
        bullets.empty()
        stats.game_active = False
        stats.level = int(stats.level) + 1
        score.make_text_level_number()
        score.draw_text_level_n()
        pygame.display.flip()
        sleep(2) #Пауза
        score.make_level()
        ship.center_ship()
        ai_setting.increase_speed() # повышение скорости игры
        stats.limit_object = 30
        stats.game_active = True
        if stats.level % 4 ==0 and ai_setting.min_objects!=7:
            ai_setting.min_objects+=1

def check_fleet_adges(aliens, ai_setting):
    '''Определяет где находится пришелец относительно краев экрана'''
    for alien in aliens.sprites():
        alien.check_edges()

def create_fleet(screen, stats, aliens, ai_setting):
    if stats.limit_object >0:
        for object in range(ai_setting.min_objects):
            alien = Alien( ai_setting, screen)
            aliens.add(alien)
        stats.limit_object -=ai_setting.delete_alien


def update_alien(aliens, ship, ai_setting, stats, screen, bullets, score, animation_object):
    '''Обновляет позицию пришельцев и обновляет игру при сталкновении'''
    check_fleet_adges(aliens, ai_setting)
    aliens.update()
    spritecollideany = pygame.sprite.spritecollideany(ship, aliens)
    if spritecollideany:
        boom = Explosion(spritecollideany.rect.center)
        animation_object.add(boom)
        ship_hit(aliens, ship, screen, stats, bullets, ai_setting, score)
    check_aliens_bottom(aliens, ship, screen, stats, bullets, ai_setting, score)

def ship_hit(aliens, ship, screen, stats, bullets, ai_setting, score):
    '''Обновление игры при сталкновении пришельцев'''
    if stats.ship_left > 0:
        stats.ship_left-=1
        #Удаление пуль и пришельцев из экрана
        aliens.empty()
        bullets.empty()

        #создание нового флота и измение перемещения в нижний центр корабль
        score.make_ships()
        stats.limit_object = 30
        ship.center_ship()
    else:
        stats.game_active=False
        pygame.mixer.music.stop()
        pygame.mouse.set_visible(True) #появление указатиля мыши на экране

def check_aliens_bottom(aliens, ship, screen, stats, bullets, ai_setting, score):
    '''Проверяет пришельцев, добрались ли они до нижнего края экрана'''
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(aliens, ship, screen, stats, bullets, ai_setting, score)
            break

def check_high_score(stats, score):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()


