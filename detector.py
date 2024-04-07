from pyautogui import pixelMatchesColor
def detect_task():
    if pixelMatchesColor(654,467,(241,212,160)):return "down/up"
    elif pixelMatchesColor(933,371,(85,98,117)):return "clean_vent"
    elif pixelMatchesColor(1147,964,(235,120,52)):return "admin_swipe"
    elif pixelMatchesColor(1424,756,(48,0,0)):return "refuel"
    elif pixelMatchesColor(1255,265,(31,72,146)): return "prime_shield"
    elif pixelMatchesColor(910,506,(253,255,92)): return "divert_power"
    elif pixelMatchesColor(527,564,(123,90,0)): return "accept_power"
    elif pixelMatchesColor(1345,558,(94,129,141)) and pixelMatchesColor(1299,563,(24,35,35)) and pixelMatchesColor(1336,512,(145,175,185)): return "garbage"
    elif pixelMatchesColor(979,540,(38,108,154)) or (pixelMatchesColor(979,540,(255,255,255)) and pixelMatchesColor(1356,640,(99,109,128))): return "stabilize_steering"
    elif pixelMatchesColor(1062,272,(137,103,0)) and pixelMatchesColor(785,604,(12,22,87)): return "wires"
    elif pixelMatchesColor(848,803,(232,240,250)) and pixelMatchesColor(1460,255,(87,87,89)): return "chart_course"
    elif pixelMatchesColor(1122,237,(255,227,0)) and pixelMatchesColor(1119,504,(83,98,255)): return "calibrate_distributor"
    elif pixelMatchesColor(1110,911,(12,30,12)) and pixelMatchesColor(1125,157,(44,45,44)): return "align_output"
    elif pixelMatchesColor(733,237,(110,12,202)) and pixelMatchesColor(733,594,(246,247,247)): return "inspect_sample_1"
    elif pixelMatchesColor(733,237,(110,12,202)) and not pixelMatchesColor(733,594,(246,247,247)): return "inspect_sample_2"