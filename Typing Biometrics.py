import time 
import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

LENGTH = 1000
WIDTH = 800

screen = pygame.display.set_mode((LENGTH,WIDTH))
pygame.display.set_caption("Typing Biometrics")

base_font = pygame.font.Font(None,30)
user_text = ''
saved = 'sd'

input_rect = pygame.Rect(500-70,400-70,140,32)

active_color = pygame.Color(255,0,0)
passive_color = pygame.Color(160,27,100,0)

verify_total_time = 0


def menu():
    global active_color, passive_color

    run = True

    r_active = False
    r_passive = True
    color = passive_color

    button_text = 'REGISTER PASSWORD'
    button_text2 = 'Verify PASSWORD'
    button_text3 = 'Login'

    register_rect = pygame.Rect((1000//2)-240/2,200,240,32)
    verify_rect = pygame.Rect((1000//2)-190/2,400,190,32)
    login_rect = pygame.Rect((1000//2)-68/2,600,68,32)    #box co-ordinates

    
    while run:
        
        image = pygame.image.load(r'C:\Users\Mr.Setu\brent\vid\2.jpg')
        image = pygame.transform.scale(image,(1000,800))

        screen.blit(image, (0, 0))
        #clock.tick(130)
        
        #pygame.display.update() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =  False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if register_rect.collidepoint(event.pos):
                    r_active = True
                    time.sleep(.1)
                    register()

                if verify_rect.collidepoint(event.pos):
                    r_active = True
                    time.sleep(.1)
                    verify()

                if login_rect.collidepoint(event.pos):
                    r_active = True
                    time.sleep(.1)
                    login()

                else:
                    r_active = False

        if r_active:
            color = active_color
        else:
            color = passive_color

        #pygame.Surface.set_alpha(register_rect)
        #pygame.draw.rect(screen, color, register_rect)
        
        #pygame.draw.rect(screen, color, verify_rect)
        #pygame.draw.rect(screen, color, login_rect)

        text_surface = base_font.render(button_text, True, (255, 255, 255))
        text_surface2 = base_font.render(button_text2, True, (255, 255, 255))
        text_surface3 = base_font.render(button_text3, True, (255, 255, 255))

        #------------------------------------------------------------------------#
        r = pygame.Surface((238,30))
        r.set_alpha(190)
        r.fill((160,27,100))

        r2 = pygame.Surface((200,30))
        r2.set_alpha(190)
        r2.fill((160,27,100))
        
        r3 = pygame.Surface((78,30))
        r3.set_alpha(190)
        r3.fill((160,27,100))

        #-------------------------------------------------------------------------#

        screen.blit(r, (register_rect.x-5, register_rect.y-1))
        screen.blit(text_surface, (register_rect.x+5, register_rect.y+5))
        
        
        screen.blit(r2, (verify_rect.x-5, verify_rect.y-1))
        screen.blit(text_surface2, (verify_rect.x+5, verify_rect.y+5))

        screen.blit(r3, (login_rect.x-5, login_rect.y-1))
        screen.blit(text_surface3, (login_rect.x+5, login_rect.y+5))
        

        #up_rects = [register_rect,verify_rect,login_rect]
        pygame.display.update()
        
       

                
                

    pygame.quit()



def register():
    global user_text, saved, input_rect
    active_color = pygame.Color(255,0,0)
    passive_color = pygame.Color(106,111,217)
    color = passive_color
    active = False
    run = True

    while run:
        r = pygame.Surface((238,30))
        r.set_alpha(190)
        r.fill((160,27,100))

        image = pygame.image.load(r'C:\Users\Mr.Setu\brent\vid\4.jpg')
        #image = pygame.transform.scale(image,(1000,800))

        screen.blit(image, (0, 0))
        #screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =  False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                    register_start_time = time.time() 
                else:
                    active = False
            if event.type == pygame.KEYDOWN and active == True :
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]

                if event.key == pygame.K_RETURN:
                    register_end_time = time.time()
                    register_total_time = register_end_time - register_start_time
                    saved = user_text
                    active = False
                    user_text = ''
                    print("r_time =" ,register_total_time)
                if event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE:
                    user_text += event.unicode
            if event.type == pygame.KEYDOWN and active == False :
                if event.key == pygame.K_BACKSPACE:
                    menu()
        
        if active:
            color = active_color
        else:
            color = passive_color

        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        
        #screen.blit(r, (input_rect.x-5, input_rect.y-1))

        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)

        pygame.display.flip()

        clock.tick(60)
        
            
    pygame.quit()


def verify():
    global saved,verify_total_time
    verify_text = ''
    verify_rect = pygame.Rect(500-70,400-70,140,32)
    verify_saved = ''
    active_color = pygame.Color(255,0,0)
    passive_color = pygame.Color(117,140,239)
    color = passive_color
    active = False
    run = True

    while run:
        image = pygame.image.load(r'C:\Users\Mr.Setu\brent\vid\5.jpg')
        #image = pygame.transform.scale(image,(1000,800))

        screen.blit(image, (0, 0))
        #screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =  False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if verify_rect.collidepoint(event.pos):
                    active = True
                    verify_start_time = time.time() 
                else:
                    active = False
            if event.type == pygame.KEYDOWN and active == True :
                if event.key == pygame.K_BACKSPACE:
                    verify_text = verify_text[:-1]

                if event.key == pygame.K_RETURN:
                    
                    verify_end_time = time.time()
                    verify_total_time = verify_end_time - verify_start_time
                    verify_saved = verify_text
                    if saved != verify_saved:
                        return('WRONG PASS!')
                    active = False
                    verify_text = ''
                    print("v_time =" ,verify_total_time)
                if event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE:
                    verify_text += event.unicode
            if event.type == pygame.KEYDOWN and active == False :
                if event.key == pygame.K_BACKSPACE:
                    menu()
        
        if active:
            color = active_color
        else:
            color = passive_color

        pygame.draw.rect(screen, color, verify_rect)
        text_surface = base_font.render(verify_text, True, (255, 255, 255))

        screen.blit(text_surface, (verify_rect.x+5, verify_rect.y+5))
        verify_rect.w = max(100, text_surface.get_width()+10)

        pygame.display.flip()

        clock.tick(60)
        
            
    pygame.quit()

b = [0,1,2]

def login():
    global saved,verify_total_time,b
    login_text = ''
    login_rect = pygame.Rect(500-70,400-70,140,32)
    login_saved = ''
    active_color = pygame.Color(255,0,0)
    passive_color = pygame.Color(8,72,188)
    color = passive_color
    active = False
    run = True


    while run:
        image = pygame.image.load(r'C:\Users\Mr.Setu\brent\vid\6.jpg')
        #image = pygame.transform.scale(image,(1000,800))

        screen.blit(image, (0, 0))
        #screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =  False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_rect.collidepoint(event.pos):
                    active = True
                    login_start_time = time.time() 
                else:
                    active = False
            if event.type == pygame.KEYDOWN and active == True :
                if event.key == pygame.K_BACKSPACE:
                    login_text = login_text[:-1]

                if event.key == pygame.K_RETURN:        #MIAN LOGIN CONDITION
                    login_end_time = time.time()
                    login_total_time = login_end_time - login_start_time
                    login_saved = login_text

                    if saved != login_saved:
                        return('WRONG PASS!')
                    
                    if login_total_time <= (verify_total_time +0.4) and login_total_time >= (verify_total_time - 0.4):
                        print('WELCOME Mr.Stark : ',login_total_time )
                        epic_win()
                    if login_total_time > (verify_total_time +0.4) or login_total_time < (verify_total_time - 0.3):
                        
                        print(login_total_time)
                        time.sleep(2)
                        a = b.pop(-1)
                        
                        if a == 0:
                            print('AUTH FAILED CHECK MAIL FOR OTP')
                            epic_loss()
                            return('MEH')
                        print(f'TRY AGAIN {a} chances remainig!')
                        
                        login()

                    active = False
                    login_text = ''
                    print("l_time =" ,login_total_time)


                if event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE:
                    login_text += event.unicode


            if event.type == pygame.KEYDOWN and active == False :
                if event.key == pygame.K_BACKSPACE:
                    menu()
        
        if active:
            color = active_color
        else:
            color = passive_color

        pygame.draw.rect(screen, color, login_rect)
        text_surface = base_font.render(login_text, True, (255, 255, 255))

        screen.blit(text_surface, (login_rect.x+5, login_rect.y+5))
        login_rect.w = max(100, text_surface.get_width()+10)

        pygame.display.flip()

        clock.tick(60)
        
            
    pygame.quit()


def epic_win():
    img1 = ['frame_000_delay-0.03s.jpg', 'frame_001_delay-0.03s.jpg', 'frame_002_delay-0.03s.jpg', 'frame_003_delay-0.03s.jpg', 'frame_004_delay-0.03s.jpg', 'frame_005_delay-0.03s.jpg', 'frame_006_delay-0.03s.jpg', 'frame_007_delay-0.03s.jpg', 'frame_008_delay-0.03s.jpg', 'frame_009_delay-0.03s.jpg', 'frame_010_delay-0.03s.jpg', 'frame_011_delay-0.03s.jpg', 'frame_012_delay-0.03s.jpg', 'frame_013_delay-0.03s.jpg', 'frame_014_delay-0.03s.jpg', 'frame_015_delay-0.03s.jpg', 'frame_016_delay-0.03s.jpg', 'frame_017_delay-0.03s.jpg', 'frame_018_delay-0.03s.jpg', 'frame_019_delay-0.03s.jpg', 'frame_020_delay-0.03s.jpg', 'frame_021_delay-0.03s.jpg', 'frame_022_delay-0.03s.jpg', 'frame_023_delay-0.03s.jpg', 'frame_024_delay-0.03s.jpg', 'frame_025_delay-0.03s.jpg', 'frame_026_delay-0.03s.jpg', 'frame_027_delay-0.03s.jpg', 'frame_028_delay-0.03s.jpg', 'frame_029_delay-0.03s.jpg', 'frame_030_delay-0.03s.jpg', 'frame_031_delay-0.03s.jpg', 'frame_032_delay-0.03s.jpg', 'frame_033_delay-0.03s.jpg', 'frame_034_delay-0.03s.jpg', 'frame_035_delay-0.03s.jpg', 'frame_036_delay-0.03s.jpg', 'frame_037_delay-0.03s.jpg', 'frame_038_delay-0.03s.jpg', 'frame_039_delay-0.03s.jpg', 'frame_040_delay-0.03s.jpg', 'frame_041_delay-0.03s.jpg', 'frame_042_delay-0.03s.jpg', 'frame_043_delay-0.03s.jpg', 'frame_044_delay-0.03s.jpg', 'frame_045_delay-0.03s.jpg', 'frame_046_delay-0.03s.jpg', 'frame_047_delay-0.03s.jpg', 'frame_048_delay-0.03s.jpg', 'frame_049_delay-0.03s.jpg', 'frame_050_delay-0.03s.jpg', 'frame_051_delay-0.03s.jpg', 'frame_052_delay-0.03s.jpg', 'frame_053_delay-0.03s.jpg', 'frame_054_delay-0.03s.jpg', 'frame_055_delay-0.03s.jpg', 'frame_056_delay-0.03s.jpg', 'frame_057_delay-0.03s.jpg', 'frame_058_delay-0.03s.jpg', 'frame_059_delay-0.03s.jpg', 'frame_060_delay-0.03s.jpg', 'frame_061_delay-0.03s.jpg', 'frame_062_delay-0.03s.jpg', 'frame_063_delay-0.03s.jpg', 'frame_064_delay-0.03s.jpg', 'frame_065_delay-0.03s.jpg', 'frame_066_delay-0.03s.jpg', 'frame_067_delay-0.03s.jpg', 'frame_068_delay-0.03s.jpg', 'frame_069_delay-0.03s.jpg', 'frame_070_delay-0.03s.jpg', 'frame_071_delay-0.03s.jpg', 'frame_072_delay-0.03s.jpg', 'frame_073_delay-0.03s.jpg', 'frame_074_delay-0.03s.jpg', 'frame_075_delay-0.03s.jpg']
    img = ['frame_00_delay-0.13s.jpg', 'frame_01_delay-0.13s.jpg', 'frame_02_delay-0.13s.jpg', 'frame_03_delay-0.13s.jpg', 'frame_04_delay-0.13s.jpg', 'frame_05_delay-0.13s.jpg', 'frame_06_delay-0.13s.jpg', 'frame_07_delay-0.13s.jpg', 'frame_08_delay-0.13s.jpg', 'frame_09_delay-0.13s.jpg', 'frame_10_delay-0.13s.jpg', 'frame_11_delay-0.13s.jpg', 'frame_12_delay-0.13s.jpg', 'frame_13_delay-0.13s.jpg', 'frame_14_delay-0.13s.jpg', 'frame_15_delay-0.13s.jpg', 'frame_16_delay-0.13s.jpg', 'frame_17_delay-0.13s.jpg', 'frame_18_delay-0.13s.jpg', 'frame_19_delay-0.13s.jpg', 'frame_20_delay-0.13s.jpg', 'frame_21_delay-0.13s.jpg', 'frame_22_delay-0.13s.jpg', 'frame_23_delay-0.13s.jpg', 'frame_24_delay-0.13s.jpg', 'frame_25_delay-0.13s.jpg', 'frame_26_delay-0.13s.jpg', 'frame_27_delay-0.13s.jpg', 'frame_28_delay-0.13s.jpg', 'frame_29_delay-0.13s.jpg', 'frame_30_delay-0.13s.jpg', 'frame_31_delay-0.13s.jpg', 'frame_32_delay-0.13s.jpg', 'frame_33_delay-0.13s.jpg', 'frame_34_delay-0.13s.jpg', 'frame_35_delay-0.13s.jpg', 'frame_36_delay-0.13s.jpg', 'frame_37_delay-0.13s.jpg', 'frame_38_delay-0.13s.jpg', 'frame_39_delay-0.13s.jpg', 'frame_40_delay-0.13s.jpg']
    gif_count = 0  
    while gif_count != 1:
        for j in img1:
            image = pygame.image.load(r'C:\Users\Mr.Setu\brent\ezgif-6-4296443cc79f-gif-im'+'\\'+j)
            image = pygame.transform.scale(image,(1000,800))

            screen.fill((255,255,255))

            screen.blit(image, (0, 0))
            
            clock.tick(24)
            pygame.display.update() 
        
        for i in img:
            image = pygame.image.load(r'C:\Users\Mr.Setu\brent'+'\\'+i)
            image = pygame.transform.scale(image,(1000,800))
            
            screen.fill((255,255,255))

            screen.blit(image, (0, 0))
        

            for event in pygame.event.get() :
        

                if event.type == pygame.QUIT :
        

                    pygame.quit()
        

                    quit()
            clock.tick(10)
            pygame.display.update() 
            if i == img[-1]:
                gif_count += 1
    menu()
    
def epic_loss():
    img1 = ['frame_072_delay-0.03s.jpg', 'frame_073_delay-0.03s.jpg', 'frame_074_delay-0.03s.jpg', 'frame_075_delay-0.03s.jpg', 'frame_076_delay-0.03s.jpg', 'frame_077_delay-0.03s.jpg', 'frame_078_delay-0.03s.jpg', 'frame_079_delay-0.03s.jpg', 'frame_080_delay-0.03s.jpg', 'frame_081_delay-0.03s.jpg', 'frame_082_delay-0.03s.jpg', 'frame_083_delay-0.03s.jpg', 'frame_084_delay-0.03s.jpg', 'frame_085_delay-0.03s.jpg', 'frame_086_delay-0.03s.jpg', 'frame_087_delay-0.03s.jpg', 'frame_088_delay-0.03s.jpg', 'frame_089_delay-0.03s.jpg', 'frame_090_delay-0.03s.jpg', 'frame_091_delay-0.03s.jpg', 'frame_092_delay-0.03s.jpg', 'frame_093_delay-0.03s.jpg', 'frame_094_delay-0.03s.jpg', 'frame_095_delay-0.03s.jpg', 'frame_096_delay-0.03s.jpg', 'frame_097_delay-0.03s.jpg', 'frame_098_delay-0.03s.jpg', 'frame_099_delay-0.03s.jpg', 'frame_100_delay-0.03s.jpg', 'frame_101_delay-0.03s.jpg', 'frame_102_delay-0.03s.jpg', 'frame_103_delay-0.03s.jpg', 'frame_104_delay-0.03s.jpg', 'frame_105_delay-0.03s.jpg', 'frame_106_delay-0.03s.jpg', 'frame_107_delay-0.03s.jpg', 'frame_108_delay-0.03s.jpg', 'frame_109_delay-0.03s.jpg', 'frame_110_delay-0.03s.jpg', 'frame_111_delay-0.03s.jpg', 'frame_112_delay-0.03s.jpg', 'frame_113_delay-0.03s.jpg', 'frame_114_delay-0.03s.jpg', 'frame_115_delay-0.03s.jpg', 'frame_116_delay-0.03s.jpg', 'frame_117_delay-0.03s.jpg', 'frame_118_delay-0.03s.jpg', 'frame_119_delay-0.03s.jpg', 'frame_120_delay-0.03s.jpg', 'frame_121_delay-0.03s.jpg', 'frame_122_delay-0.03s.jpg', 'frame_123_delay-0.03s.jpg', 'frame_124_delay-0.03s.jpg', 'frame_125_delay-0.03s.jpg', 'frame_126_delay-0.03s.jpg', 'frame_127_delay-0.03s.jpg', 'frame_128_delay-0.03s.jpg', 'frame_129_delay-0.03s.jpg', 'frame_130_delay-0.03s.jpg', 'frame_131_delay-0.03s.jpg', 'frame_132_delay-0.03s.jpg', 'frame_133_delay-0.03s.jpg', 'frame_134_delay-0.03s.jpg', 'frame_135_delay-0.03s.jpg', 'frame_136_delay-0.03s.jpg', 'frame_137_delay-0.03s.jpg', 'frame_138_delay-0.03s.jpg', 'frame_139_delay-0.03s.jpg', 'frame_140_delay-0.03s.jpg', 'frame_141_delay-0.03s.jpg', 'frame_142_delay-0.03s.jpg', 'frame_143_delay-0.03s.jpg', 'frame_144_delay-0.03s.jpg', 'frame_145_delay-0.03s.jpg', 'frame_146_delay-0.03s.jpg', 'frame_147_delay-0.03s.jpg', 'frame_148_delay-0.03s.jpg', 'frame_149_delay-0.03s.jpg', 'frame_150_delay-0.03s.jpg', 'frame_151_delay-0.03s.jpg', 'frame_152_delay-0.03s.jpg', 'frame_153_delay-0.03s.jpg', 'frame_154_delay-0.03s.jpg', 'frame_155_delay-0.03s.jpg', 'frame_156_delay-0.03s.jpg', 'frame_157_delay-0.03s.jpg', 'frame_158_delay-0.03s.jpg', 'frame_159_delay-0.03s.jpg', 'frame_160_delay-0.03s.jpg', 'frame_161_delay-0.03s.jpg', 'frame_162_delay-0.03s.jpg', 'frame_163_delay-0.03s.jpg', 'frame_164_delay-0.03s.jpg', 'frame_165_delay-0.03s.jpg', 'frame_166_delay-0.03s.jpg', 'frame_167_delay-0.03s.jpg', 'frame_168_delay-0.03s.jpg', 'frame_169_delay-0.03s.jpg', 'frame_170_delay-0.03s.jpg', 'frame_171_delay-0.03s.jpg', 'frame_172_delay-0.03s.jpg', 'frame_173_delay-0.03s.jpg', 'frame_174_delay-0.03s.jpg', 'frame_175_delay-0.03s.jpg', 'frame_176_delay-0.03s.jpg', 'frame_177_delay-0.03s.jpg', 'frame_178_delay-0.03s.jpg', 'frame_179_delay-0.03s.jpg', 'frame_180_delay-0.03s.jpg', 'frame_181_delay-0.03s.jpg', 'frame_182_delay-0.03s.jpg', 'frame_183_delay-0.03s.jpg', 'frame_184_delay-0.03s.jpg', 'frame_185_delay-0.03s.jpg', 'frame_186_delay-0.03s.jpg', 'frame_187_delay-0.03s.jpg', 'frame_188_delay-0.03s.jpg', 'frame_189_delay-0.03s.jpg', 'frame_190_delay-0.03s.jpg', 'frame_191_delay-0.03s.jpg', 'frame_192_delay-0.03s.jpg', 'frame_193_delay-0.03s.jpg', 'frame_194_delay-0.03s.jpg', 'frame_195_delay-0.03s.jpg', 'frame_196_delay-0.03s.jpg', 'frame_197_delay-0.03s.jpg', 'frame_198_delay-0.03s.jpg', 'frame_199_delay-0.03s.jpg', 'frame_200_delay-0.03s.jpg', 'frame_201_delay-0.03s.jpg', 'frame_202_delay-0.03s.jpg', 'frame_203_delay-0.03s.jpg', 'frame_204_delay-0.03s.jpg', 'frame_205_delay-0.03s.jpg', 'frame_206_delay-0.03s.jpg', 'frame_207_delay-0.03s.jpg', 'frame_208_delay-0.03s.jpg', 'frame_209_delay-0.03s.jpg', 'frame_210_delay-0.03s.jpg', 'frame_211_delay-0.03s.jpg', 'frame_212_delay-0.03s.jpg', 'frame_213_delay-0.03s.jpg', 'frame_214_delay-0.03s.jpg', 'frame_215_delay-0.03s.jpg', 'frame_216_delay-0.03s.jpg', 'frame_217_delay-0.03s.jpg', 'frame_218_delay-0.03s.jpg', 'frame_219_delay-0.03s.jpg', 'frame_220_delay-0.03s.jpg', 'frame_221_delay-0.03s.jpg', 'frame_222_delay-0.03s.jpg', 'frame_223_delay-0.03s.jpg', 'frame_224_delay-0.03s.jpg', 'frame_225_delay-0.03s.jpg', 'frame_226_delay-0.03s.jpg', 'frame_227_delay-0.03s.jpg', 'frame_228_delay-0.03s.jpg', 'frame_229_delay-0.03s.jpg', 'frame_230_delay-0.03s.jpg', 'frame_231_delay-0.03s.jpg', 'frame_232_delay-0.03s.jpg']
    img = ['frame_00_delay-0.07s.jpg', 'frame_01_delay-0.07s.jpg', 'frame_02_delay-0.07s.jpg', 'frame_03_delay-0.07s.jpg', 'frame_04_delay-0.07s.jpg', 'frame_05_delay-0.07s.jpg', 'frame_06_delay-0.07s.jpg', 'frame_07_delay-0.07s.jpg', 'frame_08_delay-0.07s.jpg', 'frame_09_delay-0.07s.jpg', 'frame_10_delay-0.07s.jpg', 'frame_11_delay-0.07s.jpg']
    gif_count = 0  
    while gif_count != 3:
        if gif_count == 0:
            for j in img1:
                image = pygame.image.load(r'C:\Users\Mr.Setu\brent\ezgif-6-4296443cc79f-gif-im'+'\\'+j)
                image = pygame.transform.scale(image,(1000,800))

                screen.fill((255,255,255))

                screen.blit(image, (0, 0))
                
                clock.tick(24)
                pygame.display.update() 
        
        for i in img:
            image = pygame.image.load(r'C:\Users\Mr.Setu\brent\ezgif-6-91f8f7f28d0d-gif-im'+'\\'+i)
            image = pygame.transform.scale(image,(1000,800))
            
            screen.fill((255,255,255))

            screen.blit(image, (0, 0))
        

            for event in pygame.event.get() :
        

                if event.type == pygame.QUIT :
        

                    pygame.quit()
        

                    quit()
            clock.tick(10)
            pygame.display.update() 
            if i == img[-1]:
                gif_count += 1
    menu()
    



def login_fail(saved,login_saved,verify_total_time,login_rect,login_text):
    global passive_color,active_color
    active = False
    color = passive_color
    run = True
    login_text2 = ''

    count = 0
    
    while run:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =  False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_rect.collidepoint(event.pos):
                    active = True
                    login_start_time = time.time() 
                else:
                    active = False

                
                
                        
                if event.type == pygame.KEYDOWN and active == True :
                    if event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE:
                        login_text2 += event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        login_text2 = login_text2[:-1]

                    if event.key == pygame.K_RETURN:        #MIAN LOGIN CONDITION
                        login_end_time = time.time()
                        login_total_time = login_end_time - login_start_time
                        login_saved = login_text2


                    if saved != login_saved:
                        return ('wrong pass')

                    
                    
                    if login_total_time <= (verify_total_time +0.4) and login_total_time >= (verify_total_time - 0.4):
                        print('WELCOME Mr.Stark: logged in try 2:',login_total_time)
                        return ('WELCOME Mr.Stark')
                    if login_total_time > (verify_total_time +0.4) or login_total_time < (verify_total_time - 0.3):
                        print('TRY AGAIN Last chances remainig!:',login_total_time)
                        login_fail2(saved,login_saved,verify_total_time,login_rect)
                    
                    active = False
                    login_text2 = ''
                    print("l_time =" ,login_total_time)

                    if event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE:
                        login_text2 += event.unicode


            if event.type == pygame.KEYDOWN and active == False :
                if event.key == pygame.K_BACKSPACE:
                    menu()
        
        if active:
            color = active_color
        else:
            color = passive_color

        pygame.draw.rect(screen, color, login_rect)
        text_surface = base_font.render(login_text2, True, (255, 255, 255))

        screen.blit(text_surface, (login_rect.x+5, login_rect.y+5))
        login_rect.w = max(100, text_surface.get_width()+10)

        pygame.display.flip()

    clock.tick(60)
                        

    pygame.quit()
    

def login_fail2(saved,login_saved,verify_total_time,login_rect):
    global passive_color,active_color
    active = False
    run = True

    count = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =  False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_rect.collidepoint(event.pos):
                    active = True
                    login_start_time = time.time() 

                if event.type == pygame.KEYDOWN and active == True :
                    if event.key == pygame.K_BACKSPACE:
                        login_text = login_text[:-1]

                    if event.key == pygame.K_RETURN:        #MIAN LOGIN CONDITION
                        login_end_time = time.time()
                        login_total_time = login_end_time - login_start_time
                        login_saved = login_text

                    login_total_time = login_time_end - login_start_time

                    if saved == login_saved:
                        login_time_end = time.time()

                    if saved != login_saved:
                        return ('wrong pass')

                    
                    
                    if login_total_time <= (verify_total_time +0.4) and login_total_time >= (verify_total_time - 0.4):
                        print('WELCOME Mr.Stark: logged in try 3:',login_total_time)
                        return ('WELCOME Mr.Stark')
                    if login_total_time > (verify_total_time +0.4) or login_total_time < (verify_total_time - 0.3):
                        print('AUTHORIZATION FAILED, CHECK MAIL FOR OTP:',login_total_time) 
                        return('bruh')   
    pygame.quit()
print(saved)
menu()


