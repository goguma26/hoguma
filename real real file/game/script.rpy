init:
    image sv normal = "sv 1.png"
    image sv surprise = "sv 2.png"
    image ev normal = "ev 1.png"
    image sangmul normal = "sangmul 1.pmg"
    image bg lab1 = "bg lab 1.png"
    image bg black = "bg black.png"
    

    define sangmul=0 #생물학과 교수 이벤 .1일경우 일어남


init python:

     #대화창 x축 마진.
    style.nvl_window.ymargin = 540
    config.searchpath.extend(['game\sound', 'game\image', 'game\music'])


# 게임에서 사용할 캐릭터
define s = Character('Dr.Steve', image = "sv")
define e = Character('이브', image = "ev")
define k = Character('김지민')#이브 가명
define g = Character('강서진')
define q = Character('???')
define t = Character('쌤 1')
define m = Character('물리학과 교수')
define sm = Character('생물학과 교수')
# 여기에서부터 게임이 시작합니다.
label start:
    "서기 2186년 "
    scene bg lab1
    show sv normal
    s " 하아….이제는 뭐하고 살아야하는 거지? rmb은행에서는 계속 빚갚으라며 난리고, 저 고철들은 시끄럽게 소리내고."
    s "이 이많은 로봇들을 모두 어떻게 해야하는거야… 만들기는 많이 만들었는데   사는 사람은 없고... 과거의 나 대체 무슨짓을 한거야!"
    scene bg black
    "3년전..."
    scene bg lab1
    show sv normal
    s "이브! 내가 만든 로봇이 지난주부터 대량 생산에 들어갔다고 연락이 온걸 지금 봤어! 이제우리는 현유회사를 이기고 부자가 되는걸 기다리고 있으면돼!"
    show ev normal
    e "축하드립니다 박사님. 이제 이것으로 많은 사람들이 박사님의 로봇을 사용하겠군요. 그리고 연락은 제발 제때받으라고 제가 항상 말씀드리지 않습니까?"
    s "알았어~ 조심한다고 했잖아. 그리고 이브 너도 수고했어. 나중에 돈들어오면 수고했으니까 네 부품을 더 좋은 부품으로 바꾸어 해줄게."
    e "감사합니다. 그것보다 샘플로봇은 작동시켜보셨나요? 전부터 제가 말씀 드렸지만 인공지능부분이 아직 미약합니다. 그래서 제가 꼭 입력해야한다고 말했던 제가 만든 프로그램은 넣으셨나요?"
    s "응? 그런게 있었어?"
    e "… 박사님 혹시 모르셨나요?"
    s "당연하지. 내가 카페인을 얼마나 먹으면서 살았는데, 솔직히 로봇 만들던 시절에 다른사람한테서 이야기를 들은게 하나도 기억이 안나."
    e "그러면 프로그램을 입력하지 않으셨던 거네요?"
    s "이브 잠시만 그 주먹내려줄수있겠어? 그래도 내가 만든 로봇은 내구도가 엄청나다고."
    e "박사님, 제가 누누히 말씀 드렸지만 가정용로봇 만드신다면서요. 그럼 내구도는 딱히 상관없어요."
    s "그, 그럼 군인 로봇으로 팔자! 내구도가 엄청나니까 전쟁무기로 쓰기 좋을거야!"
    e "이제 이세계는 전쟁이란 개념은 완전히 사라졌습니다. 예전이였으면 군인 로봇으로 대려갔을수도 있지만 당신이 저 고철덩어리 만드는 동안 세계가 달라졌어요! 제가 만든 프로그램 없으면 그냥 고철덩어리 밖에 못해요! "
    s "그럼 지금이라도 그 프로그램을 넣자!"
    e "지난주부터 생산 시작했다고 했죠?"
    s "응 그랬지"
    e "지난주 부터 생산을 시작했다고 한다면, 로봇부품 구한다고 박사님께서 돈을 다쓰셔서 공장을 일주일만 빌리시겠다고 하셨잖아요. 오늘이 딱 일주일이니까 이제 프로그램을 넣을 시간이 없.네."
    s "나중에 다시 넣으면되, 되는 거야. 괜찮아 이브."
    e "박사님, 지금도 저희 이자 밀려 있는 거 아시죠? 그거 넣으려면 공장에서 한번에 해야하는데 지금 우리는 돈이 없다고요!"
    s "그래도 시장에 팔아보면 누군가 사가줄지도 몰라."
    e "그러면 팔아보세요. 근데 제가 예상하기를 현유회사에게 밀릴겁니다. 인공지능이 잘 안돌아가는 가정용 로봇을 누가 삽니까?"
    s "한번만 해보자. 팔수있다니까."
    e "하아, 일주일동안 안팔리면 장사 접읍시다. 자리세도 내야하니까요."
    s "좋아 그러면 일주일만 기다려봐 내가 알아서 할게"
    e "좋을대로 하세요."
    "일주일 후"
    s "저기… 이브"
    e "네 박사님. 오늘까지 판매량 알려주신다고했죠? 그거나 알려주시죠. 제가 그거때문에 일주일동안 은행다니면서 시간좀 더 달라고 얼마나 힘들었는지 아십니까?"
    s "그,그래 수고했어 이브. 근데미안해… 우리 광고비밖에 회수못했어"
    e "하아"
    play music "fishing"
    s "ㅎ"
    e "ㅎ"
    s "ㅎ"
    e "ㅎ"
    s "ㅎ"
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
            play music "bacord.mp3" fadeout 0.75
            "삑."#효과음 넣어라
            play music "bacord.mp3" fadeout 0.75
            "삑."
            g "여기 막대사탕 2개, 합쳐서 500원 딱 되네요. "
            q "예?"
            g "영수증드릴까요?"
            q "아뇨, 필요없어요."
            g "'뭐지? 내가 뭐 잘못했나? 왜이렇게 기분나빠보이지?'"
            g "행복한 하루 되세요."
            "(딸랑)"
            jump iphaksik
            return
label iphaksik:
    g "아 5분만 더... 엥 벌써 시간이 8시 40분?"
    g "으아아아"
    "많은 시간이 흐른 뒤"
    t "이것으로 순살대학교 입학식을 마치겠습니다."
    g "휴...하마터면 큰일날뻔했네"
    t"이제 학생들은 각자 신청한 과 교실에서 안내받으시면 되겠습니다."
    menu:
        "물리학과":
            g "음...물리학과였지? 왜 기억이 잘 안나냐..."
            call Physics
            return

        "생물학과":
            g "음...생물학과였지? 아마도..."
            g "저쪽인가?"
            "생물학과 교실"
            g "와 저 실험쥐들 진짜 불쌍하다..."
            show sangmul normal
            sm "너 뭐냐. 우리과면 들어와라"
            g "옙"
            sm "너 이름이 뭐야."
            g "강서진 입니다."
            sm "... " #폰을 보면서 #이 생물학쌤이 가장 매력적인 캐릭터이면 좋겠음 히든 엔딩에 생물쌤 출연좀
            sm "니이름 없는데? 너 물리학과야."
            g "에?"
            sm "빨리 달려가라."
            g "으아아아 늦었다아아"
            $sangmul+=1
            jump Physicslate
            return

label Physicslate:
    g "헉 헉. 아 힘들어. 첫인상이 중요한데 교수님이 나 어떻게 생각하시려나. "
    "드르륵"
    m "뭐야 강서진. 왜 이제야와."
    g "죄송합니다."
    m "아까 그 뭐냐 걔 있잖아."
    m "어 김지민. 걔도 그렇고 오늘 얘들상태 왜이러냐."
    return


label Physics:
    g "저쪽인가?"
    "물리학과 교실"
    g "저 기구들은 다뭐지? 신기하다"
    m "오늘은 첫 날이니 앞으로 교육받을 것과 주의사항 등을 교육받도록 하겠다."
    m "출석부터 부르고 시작할까?"
    m "강서진"
    g "네!"
    "고구마" "고구마"
    고구마 "네!"
    "하리보""하리보"
    하리보 "응애!"
    m "김지민"
    "... ..."
    m "뭐야... 없어?"
    #이브가 놀란다
    k "...!"
    k "어! 접니다! 죄송합니다..."
    g "'뭐야 쟤이름이 김지민이구나.'"
    return

    #~
