﻿# 이 파일에 게임 스크립트를 입력합니다.
init python:
     #대화창에 선택지.
    menu = nvl_menu
     #대화창 x축 마진.
    style.nvl_window.ymargin = 540

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define s = Character('Dr.Steve')
define e = Character('이브')
define g = Character('강서진')
define q = Character('???')
# 여기에서부터 게임이 시작합니다.
label start:
    "서기 2186년 "
    s " 하아….이제는 뭐하고 살아야하는 거지? rmb은행에서는 계속 빚갚으라며 난리고, 저 고철들은 시끄럽게 소리내고."
    s "이 이많은 로봇들을 모두 어떻게 해야하는거야… 만들기는 많이 만들었는데   사는 사람은 없고... 과거의 나 대체 무슨짓을 한거야!"
    "3년전..."
    #여기에 과거이야기
    jump prolog

label prolog:
    "서기 2021 지구"
    "한남자가 편의점에서 일을하고있다."
    menu:

        "배경설명 듣기":
            g "대학교 입학할 자기소개나 연습해볼까..."
            g "제이름은 강서진이고 ... 할말이딱히 없네..."
            g "아니 근데 난 왜 이 사람도 잘 오지않는 이 구린 편의점에서 알바를 해야하는거지? "
            g "나 아직 대학생이야, 취직할곳도 정확히 정하지도 않았는데 엄마는 집에서 재워주는것 만으로도 고맙게 여기라면서 진짜 자식을 얼마나 강하게 키우고 싶은건데!!"
            g  "에휴, 그래도 어렸을적 부터 아빠 비상금을 조금씩 훔쳤던게 꽤 많이 모여서 지금 대학 다닐 여편은 가능하지."
            g "그거 없었으면 지금 편의점이아니라 인력소에서 일할 판이였어. 분명 자기소개 연습하려고 했는데 난 지금 뭘하고있는거지?"

        "skip":
            q "아니 열심히 썼는데 이걸 스킵하네."
    g "곧있으면 알바시간도 끝인가..."
    g "어 이거 유통기한 다 됐네. 이거나 먹어야겠다."
    "(딸랑.)"
    g "아 어서오세요 Seven25입니다."
    #여기서 이브사진을 움직여서 두리번거리는 느낌으로 그리고 이브는 '여기는 뭔가를 파는곳인가?' 이런 느낌의 표정
    g "'와 진짜예쁘다...'"
    q "혹시 여기 와이파이 있나요?"
    g "'와... 진짜 아무리봐도 예쁘다.'"
    q "저기요?"
    g "아 네! 와이파이 비밀번호는 저기 있습니다."
    g "'근데 이 망한 편의점은 왜온거지? 그 미로같은 건물들을 지나서 와야만 올수 있을텐데...'"
    q "연결됐다... 근데 여기 와이파이 왜이렇게 별로지..."
    g "'작게 말하고싶었던것 같은데 다들리네. 당연히 이 구석탱이에 박혀있는 곳이 와이파이가 좋을일이 있겠나...'"
    q "역시 그 망할녀석 집에서 대대로 물러받았다던 물건을 내가 보관하길 잘했어... 일단 가격이나 알아볼까."
    g "'이번에도 혼잣말을 하는데... 이건 뭐라하는지 잘 안들리네.'"
    q "후... 제게 시간이 별로 없습니다. 이걸로 살수있는 건 전부 주세요."
    g "'대사만 보면 뭔 돈가방을 내려놓으면서 말할것 같지만... 이사람은 왜 500원짜리 동전하나를 주면서 이런말을 할까. 일단 계산은 해야겠지.'"
    "삑."#효과음 넣어라
    "삑."
    g "여기 쥬파줍스 2개, 합쳐서 500원 딱 되네요. "
    q "예?"
    g "영수증드릴까요?"
    q "아뇨, 필요없어요."
    g "'뭐지? 내가 뭐 잘못했나? 왜이렇게 기분나빠보이지?'"
    g "행복한 하루 되세요."
    "(딸랑)"
    return
