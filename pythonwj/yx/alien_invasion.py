import sys
import pygame
from pygame.sprite import Group
from yx.settings import Settings
from yx.ship import Ship
from yx.alien import Alien
import yx.game_functions as gf
from yx.game_stats import GameStats
from yx.button import Button
from yx.scoreboard import Scoreboard
def run_game():
    # 初始化 并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一个play按钮
    play_button = Button(ai_settings,screen,"Play")
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个子弹的编组和外星人编组
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 创建统计游戏信息得分实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    # 设置背景颜色
    bg_color = ai_settings.bg_color
    # 开始主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
