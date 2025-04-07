# Triangle Conspiracy
# A mystery visual novel set in North Carolina's college triangle

################################################################################
## Initialization
################################################################################

init python:
    # Define character stats
    class PlayerStats:
        def __init__(self):
            self.intellect = 0
            self.influence = 0
            self.investigation = 0
            
    player_stats = PlayerStats()

# Define Characters
define mc = Character("[player_name]", color="#c8ffc8")
define lebron = Character("LeBron James", color="#6f2da8")
define diddler = Character("The Diddler", color="#22b14c")
define rfk = Character("RFK Jr.", color="#00a2e8")
define kendrick = Character("Kendrick Lamar", color="#ed1c24")
define drake = Character("Drake", color="#ff7f27")
define rogan = Character("Joe Rogan", color="#3f48cc")
define rowling = Character("J.K. Rowling", color="#c8bfe7")
define vick = Character("Michael Vick", color="#8b4513")
define epstein = Character("Jeffrey Epstein", color="#a349a4")
define mysterious = Character("???", color="#ffffff")

# Images - Note: In a real game, you'd replace these with actual image assets
image bg ncstate = "images/backgrounds/ncstate.png"
image bg unc = "images/backgrounds/unc.png"
image bg waketech = "images/backgrounds/waketech.png"
image bg basketball = "images/backgrounds/basketball.png"
image bg party = "images/backgrounds/party.png"
image bg lab = "images/backgrounds/lab.png"
image bg dorm = "images/backgrounds/dorm.png"
image bg office = "images/backgrounds/office.png"
image bg podcast = "images/backgrounds/podcast.png"
image bg basement = "images/backgrounds/basement.png"

image lebron neutral = "images/characters/lebron_neutral.png"
image lebron serious = "images/characters/lebron_serious.png"
image lebron smile = "images/characters/lebron_smile.png"

image diddler neutral = "images/characters/diddler_neutral.png"
image diddler smirk = "images/characters/diddler_smirk.png"
image diddler angry = "images/characters/diddler_angry.png"

image rfk neutral = "images/characters/rfk_neutral.png"
image rfk concerned = "images/characters/rfk_concerned.png"
image rfk passionate = "images/characters/rfk_passionate.png"

image kendrick neutral = "images/characters/kendrick_neutral.png"
image kendrick thoughtful = "images/characters/kendrick_thoughtful.png"
image kendrick smile = "images/characters/kendrick_smile.png"

image drake neutral = "images/characters/drake_neutral.png"
image drake smirk = "images/characters/drake_smirk.png"
image drake serious = "images/characters/drake_serious.png"

image rogan neutral = "images/characters/rogan_neutral.png"
image rogan excited = "images/characters/rogan_excited.png"
image rogan skeptical = "images/characters/rogan_skeptical.png"

image rowling neutral = "images/characters/rowling_neutral.png"
image rowling serious = "images/characters/rowling_serious.png"
image rowling smile = "images/characters/rowling_smile.png"

image vick neutral = "images/characters/vick_neutral.png"
image vick regretful = "images/characters/vick_regretful.png"
image vick determined = "images/characters/vick_determined.png"

image epstein neutral = "images/characters/epstein_neutral.png"
image epstein smirk = "images/characters/epstein_smirk.png"
image epstein angry = "images/characters/epstein_angry.png"

################################################################################
## The game starts here
################################################################################

label start:
    # Character creation
    $ player_name = renpy.input("What is your name?", "", allow=None)
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name = "Taylor"
    
    scene bg dorm
    with fade
    
    "Welcome to the North Carolina college triangle, where three prestigious institutions compete for academic glory."
    "You're a journalism student who's landed an internship with a major investigation into corruption across NC's college basketball programs."
    "What begins as a sports story will soon take you down a rabbit hole of conspiracy that connects celebrities, politics, and dark secrets."
    
    menu:
        "Choose your background:"
        
        "Investigative Journalism (Investigation +2, Intellect +1)":
            $ player_stats.investigation += 2
            $ player_stats.intellect += 1
            "You've always had a nose for uncovering hidden truths. Your keen attention to detail will be valuable."
            
        "Social Media Influencer (Influence +2, Investigation +1)":
            $ player_stats.influence += 2
            $ player_stats.investigation += 1
            "Your large online following gives you connections and platforms that most journalists would envy."
            
        "Academic Researcher (Intellect +2, Influence +1)":
            $ player_stats.intellect += 2
            $ player_stats.influence += 1
            "Your rigorous training in research methodology helps you analyze complex information systematically."
    
    jump day_one

label day_one:
    scene bg ncstate
    with fade
    
    "Day 1: NC State University"
    
    "The autumn air is crisp as you walk through the NC State campus, notebook in hand. Your editor wants you to look into rumors of recruiting violations."
    
    "Your first interview is with a former NBA star who's been mentoring young players and has expressed concerns about the system."
    
    scene bg basketball
    with fade
    
    show lebron neutral at right
    with dissolve
    
    lebron "Appreciate you taking the time to cover this story. Not many journalism students want to rock the boat."
    
    mc "Thanks for meeting with me, Mr. James. I'm interested in what you've seen in college recruitment."
    
    show lebron serious
    
    lebron "Look, the system's broken. These colleges make millions off these kids while they get nothing but 'education'—if they even attend classes."
    
    lebron "But that's just the surface. There's darker stuff happening that nobody wants to talk about."
    
    menu:
        "Ask about specific violations":
            $ player_stats.investigation += 1
            mc "Do you have evidence of specific recruiting violations at NC State?"
            
            show lebron neutral
            
            lebron "I'm not here to name names yet. But I'll tell you this—follow the money. Especially around the big tournaments."
            
            lebron "There's a party happening tonight at the Delta house. The Diddler will be there, and he knows things about the boosters."
            
            mc "The Diddler? You mean..."
            
            lebron "Yeah, he's taken on this weird persona lately. But beneath the riddles, he's connected to everyone with money in college sports."
            
        "Ask about the 'darker stuff'":
            $ player_stats.intellect += 1
            mc "What do you mean by 'darker stuff'? That sounds concerning."
            
            show lebron serious
            
            lebron "These young athletes get pulled into circles they're not prepared for. Parties with powerful people, politicians, entertainers."
            
            lebron "There's a guy—calls himself 'The Diddler' now—who's at the center of it all. Throwing parties, connecting people who shouldn't be connected."
            
            lebron "He's hosting something tonight at the Delta house. If you want to see how deep this goes, start there."
    
    show lebron neutral
    
    lebron "One more thing. Talk to Michael Vick when you get a chance. He's giving a talk about second chances at Wake Tech tomorrow."
    
    lebron "He went through the system and saw the corruption firsthand. He's been trying to warn new players."
    
    mc "Why are you telling me all this? Aren't you worried about backlash?"
    
    show lebron smile
    
    lebron "I've made my money. I can take the heat. These college kids can't. Someone needs to change the system."
    
    hide lebron
    with dissolve
    
    "As LeBron walks away, your phone buzzes with a campus alert."
    
    "'Distinguished guest lecture tonight at Davidson Hall by RFK Jr. on 'Academic Freedom and Scientific Integrity.' All students welcome.'"
    
    menu:
        "Attend RFK Jr.'s lecture":
            jump rfk_lecture
            
        "Go to the Delta house party":
            jump delta_party

label rfk_lecture:
    scene bg ncstate
    with fade
    
    "The lecture hall is packed with students from all three area schools. The atmosphere is charged, with both supporters and protesters."
    
    show rfk neutral at center
    with dissolve
    
    rfk "Thank you all for coming tonight. In a time when academic freedom is under attack, we need open and honest dialogue more than ever."
    
    "His lecture touches on controversial research being suppressed at universities, corporate influence on studies, and the erosion of scientific integrity."
    
    show rfk passionate
    
    rfk "What you don't know is that right here, in the Research Triangle, experiments are being conducted that violate every ethical standard we have."
    
    rfk "I've obtained documents showing a collaboration between pharmaceutical companies and researchers across all three major institutions."
    
    "A murmur runs through the crowd. Some people look uncomfortable, others skeptical."
    
    show rfk concerned
    
    rfk "And the funding? It traces back to shell companies connected to people who supposedly aren't even alive anymore."
    
    menu:
        "Ask about the documents":
            $ player_stats.investigation += 1
            mc "You mentioned documents. Can you share any evidence of these claims?"
            
            show rfk neutral
            
            rfk "I have sources inside the research programs. Meet me after the lecture, and I'll give you copies."
            
            rfk "But be careful who sees you with them. There are powerful people who don't want this exposed."
            
        "Ask about the 'supposedly dead' funders":
            $ player_stats.intellect += 1
            mc "You implied some of the funders are supposedly deceased? Who were you referring to?"
            
            show rfk concerned
            
            rfk "There's a reason I chose my words carefully. Let's just say a certain financier who allegedly died in prison continues to have an unusual influence on research funding."
            
            rfk "The money trail leads to private islands and then back to grants at UNC and NC State."
    
    "After the lecture, a small group forms around RFK Jr., including several skeptical faculty members."
    
    show rowling neutral at left
    with dissolve
    
    show rfk neutral at right
    with move
    
    rowling "While I appreciate your passion for academic freedom, these accusations require extraordinary evidence."
    
    rowling "As a visiting professor in ethics, I cannot condone spreading conspiracy theories to impressionable students."
    
    show rfk passionate
    
    rfk "With respect, Professor Rowling, skepticism is healthy. But dismissing evidence as 'conspiracy theory' is exactly how powerful interests shield themselves."
    
    rfk "Ask yourself why certain research proposals get fast-tracked while others languish in review for years."
    
    show rowling serious
    
    rowling "There's a difference between justified critique and dangerous misinformation. These students deserve better."
    
    "The tension between them is palpable. You make a note to follow up with Professor Rowling later."
    
    hide rowling
    with dissolve
    
    show rfk neutral at center
    with move
    
    "As the crowd disperses, RFK Jr. approaches you."
    
    rfk "You asked good questions. There's more to this story than I could share publicly."
    
    rfk "There's a party tonight at Delta house. The Diddler will be there—he's connected to all of this. If you want the full picture, you should go."
    
    rfk "And find me tomorrow at UNC's medical research building. I'll have those documents for you."
    
    hide rfk
    with dissolve
    
    menu:
        "Go to the Delta house party now":
            jump delta_party
            
        "Research The Diddler first":
            $ player_stats.intellect += 1
            
            "You decide to do some quick research before heading to the party."
            
            "Multiple news articles reference his bizarre transition from music mogul to self-styled villain character, complete with question-mark themed outfits."
            
            "More concerning are the sealed court cases and rumors of misconduct spanning decades."
            
            "One blog claims he's been spotted meeting with several prominent figures at NC colleges, including some faculty who received sudden grant funding."
            
            "Armed with this background, you head to the Delta house."
            
            jump delta_party

label delta_party:
    scene bg party
    with fade
    
    "The Delta house is pulsing with music and packed with students, athletes, and some faces you recognize from TV and social media."
    
    "In one corner, Drake is surrounded by basketball players, taking selfies and laughing."
    
    "Near the bar, Joe Rogan is engaged in an intense conversation with several students."
    
    "You scan the room for The Diddler."
    
    show diddler neutral at center
    with dissolve
    
    "A man in an outlandish green suit decorated with purple question marks approaches you. His smile is uncomfortable."
    
    diddler "Well, well. A new face with a notebook. Riddle me this: What has eyes but cannot see what's right in front of them?"
    
    mc "I'm guessing... a journalism student?"
    
    show diddler smirk
    
    diddler "Sharp! I like that. Yes, a journalist who only sees what they're allowed to see."
    
    diddler "But you're different, aren't you? LeBron sent you. Or was it Kennedy? Both men who think they can change systems built by people far more powerful than them."
    
    menu:
        "Ask about his connection to NC State":
            $ player_stats.investigation += 1
            mc "What's your interest in college basketball? I hear you're connected to the boosters."
            
            show diddler neutral
            
            diddler "Basketball, football, research grants... I'm interested in potential. Young talent that can be... cultivated."
            
            diddler "NC State has particular potential. Do you know about the underground facility beneath the science building? Fascinating research."
            
            mc "What kind of research?"
            
            show diddler smirk
            
            diddler "The kind that changes people. Enhances them. Ask your friend Kennedy about it tomorrow."
            
        "Ask about the parties and powerful people":
            $ player_stats.influence += 1
            mc "I hear you connect athletes to some influential circles. What exactly happens at these gatherings?"
            
            show diddler smirk
            
            diddler "Networking, my curious friend! Stars meet financiers meet politicians. The real decisions about who succeeds in this world aren't made in offices."
            
            diddler "Take Drake over there. He identifies promising talent for me. Kendrick, though—he's become a problem. Too many questions, like you."
            
            "He nods toward another corner where Kendrick Lamar stands alone, observing the party with obvious discomfort."
    
    show diddler neutral
    
    diddler "Enough about me. Riddle me this: What connects an allegedly dead financier, experimental treatments, and championship trophies?"
    
    mc "I don't know. What?"
    
    show diddler smirk
    
    diddler "That's your riddle to solve! But here's a clue: Visit Wake Tech's new sports medicine facility. Ask about 'Project Phoenix.' Tell them The Diddler sent you."
    
    diddler "Now if you'll excuse me, I need to chat with our friends from UNC's administration. So much potential there too!"
    
    hide diddler
    with dissolve
    
    "The Diddler walks away to join a group of serious-looking older men in suits."
    
    menu:
        "Talk to Drake":
            $ player_stats.influence += 1
            
            show drake neutral at right
            with dissolve
            
            mc "Excuse me, Drake? I'm doing a story on college athletics. Got a minute?"
            
            drake "Always time for the press, you know how it is. What's your angle?"
            
            mc "I'm looking into recruiting practices and some concerns about how athletes are treated."
            
            show drake smirk
            
            drake "Man, that's a deep pool you're diving into. These schools make billions off these kids."
            
            drake "I do what I can, you know? Mentor some of them, show them how to build their brand outside the system."
            
            mc "And The Diddler? What's his role?"
            
            show drake serious
            
            drake "Word of advice? Be careful with that line of questioning. Some doors are better left closed."
            
            drake "But if you're determined, talk to Kendrick. He's been researching something about all three schools and their medical programs."
            
            hide drake
            with dissolve
            
        "Talk to Kendrick":
            $ player_stats.intellect += 1
            
            show kendrick neutral at left
            with dissolve
            
            mc "Kendrick Lamar? I'm a journalism student working on a story."
            
            kendrick "Another one asking questions. Good. Not enough people doing that these days."
            
            mc "The Diddler mentioned you've become a 'problem.' What's that about?"
            
            show kendrick thoughtful
            
            kendrick "I started sponsoring basketball programs, trying to help kids. Then I saw how deep it goes."
            
            kendrick "You think it's just about money? Nah. It's experiments. Enhancements. These schools are using athletes as test subjects."
            
            mc "That sounds like a serious accusation."
            
            show kendrick thoughtful
            
            kendrick "Meet me tomorrow at UNC's library. I've compiled documents, testimonies from former players. Evidence about 'Project Phoenix.'"
            
            kendrick "And watch your back. Last journalist who looked into this suddenly got a dream job offer overseas."
            
            hide kendrick
            with dissolve
    
    "As the party continues, you notice Joe Rogan waving you over."
    
    show rogan neutral at center
    with dissolve
    
    rogan "Hey, I overheard you asking questions. You're that journalism student, right? You should come on my podcast tomorrow."
    
    rogan "I'm recording at Wake Tech with Michael Vick. We're discussing the college sports system and some weird stuff happening in the medical programs."
    
    mc "What kind of weird stuff?"
    
    show rogan excited
    
    rogan "Performance enhancements, experimental recoveries. I had this doctor on who spoke about cellular regeneration techniques being tested on athletes without proper consent."
    
    rogan "Vick knows some players who went through it. JK Rowling's been trying to raise ethical concerns too, but keeps getting shut down."
    
    menu:
        "Accept podcast invitation":
            $ player_stats.influence += 2
            mc "I'd be honored to join your podcast. I could share what I've learned so far."
            
            show rogan excited
            
            rogan "Perfect! Tomorrow, 2 PM at Wake Tech's media center. Bring your notes."
            
            rogan "And listen, be careful with The Diddler. That dude's connected to some seriously powerful people. Including some who should be in prison. Or already supposed to be dead."
            
        "Ask for more information":
            $ player_stats.investigation += 1
            mc "Before I commit, what exactly do you know about these experiments?"
            
            show rogan skeptical
            
            rogan "It's all about recovery times. Players getting back on the court after injuries that should take months to heal."
            
            rogan "And there's this guy—supposedly dead—whose foundation keeps funding these programs. Private island guy, if you catch my drift."
            
            rogan "The research is happening across all three schools, but Wake Tech's new facility is where they're scaling it up. Check it out."
    
    show rogan neutral
    
    rogan "Whatever you do, don't miss Vick's talk tomorrow. He's going to blow the lid off some of this, and I don't think 'they' know what he's planning to say."
    
    hide rogan
    with dissolve
    
    "As the night progresses, you collect business cards, record conversations, and observe interactions."
    
    "One thing becomes clear: there's an intricate web connecting these celebrities, the colleges, and something called 'Project Phoenix.'"
    
    scene bg dorm
    with fade
    
    "Back in your dorm room, you organize your notes and plan for tomorrow."
    
    "Three paths seem promising:"
    
    menu:
        "Follow up with RFK Jr. at UNC":
            $ player_stats.investigation += 1
            "You decide to prioritize getting those documents from RFK Jr. tomorrow."
            jump day_two_unc
            
        "Attend Michael Vick's talk at Wake Tech":
            $ player_stats.intellect += 1
            "Vick's inside perspective on the system seems most valuable for your investigation."
            jump day_two_waketech
            
        "Investigate 'Project Phoenix' at the sports medicine facility":
            $ player_stats.influence += 1
            "The mysterious project seems to be at the center of everything."
            jump day_two_project

label day_two_unc:
    scene bg unc
    with fade
    
    "Day 2: UNC Chapel Hill"
    
    "The UNC campus is beautiful in the morning light. You head to the medical research building where RFK Jr. said he would meet you."
    
    "As you approach, you notice campus security seems unusually present today."
    
    "Your phone buzzes with a text from an unknown number: 'Meeting location changed. Come to the old library stacks. Third floor. -R'"
    
    menu:
        "Go to the new location":
            $ player_stats.investigation += 1
            
            scene bg office
            with fade
            
            "The old library stacks are quiet and dimly lit. You take the stairs to the third floor."
            
            show rfk concerned at right
            with dissolve
            
            rfk "Thank you for coming. I couldn't meet at the medical building. They've increased security since last night."
            
            mc "What's going on?"
            
            rfk "After my lecture, someone broke into my hotel room. They were looking for these."
            
            "He hands you a USB drive and a folder of documents."
            
            rfk "These are research protocols for 'Project Phoenix' - a cellular regeneration treatment being tested on athletes without proper informed consent."
            
            rfk "The funding traces back to shell companies connected to Jeffrey Epstein's estate."
            
            mc "But Epstein is dead."
            
            show rfk neutral
            
            rfk "Is he? There are documented sightings. And more importantly, his network continues to operate."
            
        "Call RFK Jr. to verify":
            $ player_stats.intellect += 1
            
            "You decide to call RFK Jr.'s official number to verify the text."
            
            "No answer. You leave a message and wait in the lobby of the medical building."
            
            "Twenty minutes later, he calls back."
            
            rfk "Sorry I missed you. Yes, I sent that text. There's been a development. Meet me at the old library."
            
            scene bg office
            with fade
            
            show rfk concerned at right
            with dissolve
            
            rfk "Someone broke into my hotel room last night looking for these documents. We need to be careful."
            
            "He hands you a USB drive and a folder."
            
            rfk "This is evidence of unethical medical research happening across all three schools, funded by shell companies linked to Epstein."
    
    show rfk passionate
    
    rfk "Project Phoenix isn't just about healing athletes faster. It's about perfecting techniques that can... well, the implications are disturbing."
    
    rfk "The technology could potentially extend life indefinitely, but only for those who can afford it."
    
    mc "That sounds like science fiction."
    
    show rfk neutral
    
    rfk "Five years ago, I would have agreed. But the preliminary results are real. Athletes recovering from career-ending injuries in weeks instead of months."
    
    "Suddenly, you hear voices approaching."
    
    rfk "We need to go. Meet me at Rogan's podcast recording later at Wake Tech. I'll bring more evidence."
    
    hide rfk
    with dissolve
    
    show rowling neutral at left
    with dissolve
    
    rowling "I thought I heard voices in here. [player_name], isn't it? From the lecture last night?"
    
    mc "Professor Rowling. Yes, I'm working on a story about college athletics."
    
    show rowling serious
    
    rowling "In the restricted stacks? Curious place for sports journalism."
    
    rowling "I notice Kennedy has been filling your head with his theories. Let me offer some advice: distinguish between genuine concerns about academic freedom and dangerous conspiracy thinking."
    
    menu:
        "Defend RFK Jr.":
            $ player_stats.investigation += 1
            mc "He showed me documents about Project Phoenix. They seem credible."
            
            show rowling neutral
            
            rowling "Project Phoenix is a legitimate medical research initiative into accelerated healing. Yes, there are ethical questions, which is why I'm on the oversight committee."
            
            rowling "The wild connections to deceased financiers and immortality treatments? That's where it veers into fantasy."
            
            rowling "Be careful about what you publish. Careers have been ruined by less."
            
        "Play neutral":
            $ player_stats.intellect += 1
            mc "I'm gathering perspectives from all sides. What's your take on these research programs?"
            
            show rowling smile
            
            rowling "A responsible approach. Project Phoenix is groundbreaking medical research with strict ethical oversight."
            
            rowling "Yes, it's received private funding through various foundations. That's how modern research works."
            
            rowling "If you're serious about understanding this, come to my ethics lecture at Wake Tech this afternoon. I can introduce you to the actual researchers."
    
    show rowling neutral
    
    rowling "One more thing. If Kendrick Lamar contacts you—he's been making similar accusations—know that he's motivated by a personal vendetta after his cousin was dismissed from the basketball program."
    
    "She walks away, leaving you with more questions than answers."
    
    hide rowling
    with dissolve
    
    "Your phone buzzes with a text from Kendrick: 'Need to talk. Vick's lecture at Wake Tech. Meet me there.'"
    
    jump day_two_waketech

label day_two_waketech:
    scene bg waketech
    with fade
    
    "Wake Tech Community College is buzzing with activity. Michael Vick's talk on second chances has drawn a large crowd."
    
    "You notice several basketball players from both NC State and UNC in attendance."
    
    scene bg office
    with fade
    
    show vick neutral at center
    with dissolve
    
    vick "Thank you all for coming today. My journey has been about redemption and recognizing systems of exploitation."
    
    vick "When I was coming up, I made terrible mistakes because I was part of a system that didn't value me as a person—only as a talent."
    
    vick "Today's athletes face similar pressures, but there are new dangers. Coaches, boosters, sponsors pushing boundaries to get performance."
    
    show vick regretful
    
    vick "I've counseled players who were pressured into experimental treatments. Promised faster recovery, better performance. Not told about the risks."
    
    "He looks directly at several athletes in the audience."
    
    vick "Some of you know exactly what I'm talking about. Project Phoenix isn't just about healing. It's about creating superhuman performance at any cost."
    
    "A murmur runs through the crowd. Some people shift uncomfortably."
    
    menu:
        "Record the lecture":
            $ player_stats.investigation += 1
            
            "You discreetly begin recording as Vick continues."
            
            show vick determined
            
            vick "I've seen the facilities. Hidden labs beneath the main sports medicine buildings at all three schools."
            
            vick "Athletes signing papers they don't understand, getting injections that aren't FDA approved."
            
            vick "And the money behind it? Coming from people like The Diddler and foundations connected to a man who supposedly died in prison."
            
            "Several people in suits at the back of the room are speaking urgently into their phones."
            
        "Take detailed notes":
            $ player_stats.intellect += 1
            
            "You write frantically as Vick reveals more details."
            
            show vick determined
            
            vick "The treatments started with simple recovery acceleration. Now they're moving into genetic modification territory."
            
            vick "Players reporting strange side effects. Mood changes, dependency, blackouts."
            
            vick "And it all connects back to research that was supposedly shut down years ago after ethical violations. Research originally funded by Jeffrey Epstein."
    
    show vick neutral
    
    vick "If you're an athlete being pressured into these programs, come talk to me. I have lawyers ready to help protect you."
    
    "As the lecture ends, you notice Joe Rogan entering from the side door, setting up for his podcast."
    
    show rogan neutral at right
    with dissolve
    
    show vick neutral at left
    with move
    
    rogan "Powerful stuff, man. You ready to go deeper on the podcast?"
    
    vick "Ready as I'll ever be. They're gonna try to discredit me after this."
    
    rogan "Let them try. We've got the documents, the witness testimonies."
    
    "They notice you approaching."
    
    rogan "Hey, the journalism student! Perfect timing. You still want to join us for the recording?"
    
    menu:
        "Join the podcast":
            $ player_stats.influence += 2
            mc "Absolutely. I've been gathering information about Project Phoenix myself."
            
            show rogan excited
            
            rogan "Perfect! We're going live in 30 minutes. This is going to blow people's minds."
            
            show vick determined
            
            vick "Just be prepared for blowback. Once this gets out, they'll come after all of us."
            
            scene bg podcast
            with fade
            
            "The podcast setup is professional but intimate. As you prepare to go live, Kendrick Lamar and RFK Jr. arrive to join the panel."
            
            "Just before recording starts, your phone buzzes with a text: 'URGENT - Meet me at the sports medicine building basement. Evidence being destroyed. -Unknown'"
            
        "Check out the sports medicine facility first":
            $ player_stats.investigation += 1
            mc "Actually, I think I should see this facility for myself before we record. Is it nearby?"
            
            show rogan neutral
            
            rogan "Smart move. Get the firsthand look. It's the new building across the quad."
            
            show vick neutral
            
            vick "Use my name if anyone stops you. Say you're interviewing me about my rehabilitation process."
            
            vick "Try to get to the basement level. That's where the real work happens."
            
            rogan "We go live in an hour. Get back here with what you find, and we'll break it on air."
    
    jump day_two_project

label day_two_project:
    scene bg waketech
    with fade
    
    "The new sports medicine facility is sleek and modern—clearly well-funded."
    
    "A sign reads 'Phoenix Recovery Center: Tomorrow's Healing Today'"
    
    "The reception area is quiet, with athletes coming and going for various treatments."
    
    "You approach the front desk."
    
    mc "Hi, I'm working on a story about advanced recovery techniques. I'm particularly interested in Project Phoenix."
    
    "The receptionist freezes momentarily."
    
    "Receptionist" "Do you have an appointment? That particular research program is restricted."
    
    menu:
        "Mention The Diddler":
            $ player_stats.influence += 1
            mc "The Diddler sent me. He suggested I look into the program."
            
            "The receptionist's expression changes immediately."
            
            "Receptionist" "One moment please."
            
            "She makes a phone call, speaking quietly."
            
            "Receptionist" "Someone will be with you shortly. Please wait."
            
            "Ten minutes later, a researcher in a lab coat appears."
            
            "Researcher" "I understand you're here about Project Phoenix. The Diddler mentioned you would be coming."
            
            "Researcher" "I can give you a tour of our standard facilities, but for the specialized research areas, you'll need clearance."
            
        "Mention Michael Vick":
            $ player_stats.investigation += 1
            mc "I'm interviewing Michael Vick about his rehabilitation process. He suggested I check out your facilities."
            
            "The receptionist looks uncertain."
            
            "Receptionist" "Mr. Vick has been here, yes. Let me see if Dr. Matthews is available to speak with you."
            
            "After a brief wait, a nervous-looking doctor appears."
            
            "Dr. Matthews" "You're with Vick? He wasn't supposed to bring press here. But since you're already here, I can show you our public recovery facilities."
    
    "You're led through the main facility, shown therapy pools, high-tech equipment, and recovery rooms."
    
    "Throughout the tour, you notice security keypads on certain doors, and areas marked 'Authorized Personnel Only.'"
    
    mc "What about the basement level? I understand there's specialized research happening there."
    
    "Your guide becomes visibly uncomfortable."
    
    "Guide" "The basement houses technical equipment only. Nothing of interest."
    
    "As you're walking, your phone buzzes again. A text from the same unknown number: 'Storage closet, end of east hall. Key code 1729.'"
    
    menu:
        "Create a distraction":
            $ player_stats.influence += 1
            
            "You pretend to receive an urgent call and step away from the tour."
            
            mc "Sorry, I need to take this. It's my editor. I'll catch up with you."
            
            "Your guide hesitates but nods, continuing with the prepared tour route."
            
            "You quickly find the east hall and locate the storage closet."
            
            "You enter the code: 1729."
            
            "The door unlocks with a click."
            
        "Ask direct questions":
            $ player_stats.investigation += 1
            
            mc "Let's be direct. I know about the experimental treatments happening in the basement. Athletes with impossible recovery times."
            
            "Your guide looks around nervously."
            
            "Guide" "I don't know what you're talking about. But if I were you, I'd be very careful about making accusations without evidence."
            
            "Guide" "Wait here. I need to speak with my supervisor."
            
            "The moment they leave, you dash toward the east hall, finding the storage closet."
            
            "You input the code: 1729."
            
            "The door opens."
    
    scene bg basement
    with fade
    
    "Inside the closet is a maintenance elevator. You take it down to the basement level."
    
    "The doors open to a sterile, high-tech laboratory environment—nothing like the sports recovery facility upstairs."
    
    "You hear voices and duck behind some equipment."
    
    show rowling serious at left
    with dissolve
    
    show epstein neutral at right
    with dissolve
    
    epstein "Kennedy and Vick are becoming serious problems. And now this student journalist is poking around."
    
    rowling "I warned you about expanding too quickly. The basketball program was one thing, but scaling to all three schools attracted too much attention."
    
    epstein "We can't stop now. The trials are showing unprecedented success. Cellular regeneration at rates we never imagined."
    
    epstein "The immortality protocol is nearly perfected."
    
    rowling "And the side effects? The athletes experiencing blackouts, personality changes?"
    
    show epstein smirk
    
    epstein "Acceptable losses for progress. Besides, they signed the waivers."
    
    rowling "Waivers they couldn't possibly understand. This is unethical, and you know it."
    
    show epstein neutral
    
    epstein "Ethics didn't build empires, Professor Rowling. Results did. The Diddler is bringing three new test subjects tonight."
    
    epstein "Once we perfect the serum, think about it—eternal life for those who can afford it."
    
    "You accidentally knock over a tray of equipment."
    
    show epstein angry
    
    epstein "Who's there?"
    
    show rowling angry
    
    rowling "It's the journalist!"
    
    menu:
        "Run for the elevator":
            $ player_stats.investigation += 1
            
            "You sprint back toward the elevator, fumbling with the controls."
            
            "Behind you, security alarms begin to blare."
            
            "Just as the elevator doors close, you see Epstein and Rowling rushing toward you."
            
            scene bg waketech
            with fade
            
            "You burst out of the facility, heart pounding."
            
            "Your phone buzzes with texts from Rogan and Kendrick, wondering where you are."
            
            "You have what you need—confirmation that Epstein is alive and running Project Phoenix."
            
        "Take photos":
            $ player_stats.intellect += 1
            
            "You quickly snap photos of the lab and the two conspirators with your phone."
            
            "The flash gives you away completely."
            
            show epstein angry
            
            epstein "Stop them! Security!"
            
            "You run for the exit as alarms blare throughout the facility."
            
            "Guards appear at the elevator, but you spot an emergency stairwell."
            
            "You burst through the doors and sprint up the stairs, emerging in a side hallway of the main building."
    
    "You race across campus toward the media center where Rogan's podcast is about to begin."
    
    scene bg podcast
    with fade
    
    show rogan neutral at left
    show vick neutral at center
    show kendrick neutral at right
    with dissolve
    
    "You burst into the studio, out of breath."
    
    mc "He's alive! Epstein is alive, and he's running Project Phoenix!"
    
    show rogan shocked
    
    rogan "Whoa, slow down! What did you find?"
    
    mc "I got into the basement lab. I saw him with Rowling, discussing the immortality serum they're testing on athletes."
    
    show kendrick thoughtful
    
    kendrick "I told you all. This goes beyond sports."
    
    show vick shocked
    
    vick "Did you get proof? Recordings? Photos?"
    
    menu:
        "Show your evidence":
            if player_stats.investigation > 5:
                "You pull out your phone, showing the photos and playing a recording you managed to capture."
                
                show rogan excited
                
                rogan "This is incredible. We need to get this out immediately."
                
                kendrick "Once we broadcast this, there's no going back. They'll come for all of us."
                
                mc "People need to know the truth."
                
                show vick determined
                
                vick "Let's do it."
                
            else:
                "You show what evidence you have, but it's somewhat inconclusive."
                
                show rogan skeptical
                
                rogan "It's compelling, but we need more to make these kinds of accusations."
                
                show kendrick thoughtful
                
                kendrick "I've been gathering evidence too. Between all of us, we might have enough."
                
                vick "We need to be careful. These are powerful people."
                
        "Describe what you saw":
            $ player_stats.influence += 1
            
            "You describe the laboratory, the conversation you overheard, and Epstein's presence in detail."
            
            show rogan skeptical
            
            rogan "That's a massive claim. We need hard evidence before we go public."
            
            show kendrick neutral
            
            kendrick "I believe you. It matches everything I've found."
            
            show vick determined
            
            vick "If what you're saying is true, we need to act now. More athletes are being recruited for these experiments tonight."
    
    "As you're planning what to do next, the studio door bursts open."
    
    show rfk determined at left
    with dissolve
    
    show rogan neutral at center
    with move
    
    show vick neutral at right
    with move
    
    show kendrick neutral at right
    with moveinright
    
    rfk "They're coming! Campus security and private guards, heading this way."
    
    rfk "The Diddler is with them. They know we're planning to expose everything."
    
    mc "What do we do?"
    
    rfk "I've contacted federal authorities. But they won't be here in time."
    
    show kendrick thoughtful
    
    kendrick "I've been streaming everything to my followers. Over a million people are watching right now."
    
    show rogan excited
    
    rogan "Let's go live with what we have. Once it's out there, they can't put the genie back in the bottle."
    
    scene bg confrontation
    with fade
    
    show diddler angry at center
    with dissolve
    
    show epstein angry at left
    with dissolve
    
    "The door crashes open. The Diddler and Epstein enter, flanked by security guards."
    
    diddler "Riddle me this: What's the sound of a career ending?"
    
    epstein "This is a serious mistake you're all making. We're developing medical technologies that will change humanity forever."
    
    show rogan neutral at right
    with dissolve
    
    rogan "By experimenting on unconsenting athletes? By faking your death to avoid justice?"
    
    show kendrick neutral at right
    with dissolve
    
    kendrick "It's too late. The world is watching now."
    
    show epstein smirk
    
    epstein "You think exposing us changes anything? The powerful protect their own."
    
    show diddler smirk
    
    diddler "We'll simply relocate. So many ambitious universities, so many desperate athletes."
    
    menu:
        "Appeal to Rowling":
            if player_stats.intellect > 4:
                mc "Professor Rowling, you know this is wrong. You're an ethicist. You can stop this."
                
                show rowling serious at left
                with dissolve
                
                show epstein angry at center
                with move
                
                rowling "I've been trying to reform from within. But you're right. This has gone too far."
                
                rowling "I've been documenting everything. All the violations, all the cover-ups."
                
                show epstein angry
                
                epstein "Joanne, don't be a fool!"
                
                show rowling determined
                
                rowling "No more. I'm done being complicit."
                
            else:
                mc "Professor Rowling wouldn't support this if she knew the full truth!"
                
                show diddler smirk
                
                diddler "Oh, but she does! Our ethical watchdog has been thoroughly muzzled."
                
                epstein "Some principles have a price tag. Hers was quite reasonable."
                
        "Signal to Lebron":
            if player_stats.influence > 4:
                "You notice Lebron James and several other athletes at the doorway, livestreaming on their phones."
                
                show lebron serious at right
                with dissolve
                
                lebron "We heard everything. All the athletes are walking out, right now."
                
                lebron "No more games, no more experiments. It's over."
                
                show diddler angry
                
                diddler "You can't walk away from contracts!"
                
                show lebron smile
                
                lebron "Watch us."
                
            else:
                "You try to signal for help, but you're surrounded."
                
                show drake nervous at right
                with dissolve
                
                drake "Man, this is getting crazy. I never signed up for mad scientist stuff."
                
                drake "I was just supposed to spot talent, not feed kids to experiments."
                
                show diddler angry
                
                diddler "Shut up, you fool!"
    
    "Suddenly, federal agents burst through the doors."
    
    "Agent" "FBI! Everyone freeze!"
    
    show epstein defeated
    
    epstein "This isn't over. You have no idea how deep this goes, how many powerful people are involved."
    
    show diddler defeated
    
    diddler "Riddle me this: How long can secrets stay buried? The answer: Not forever."
    
    scene bg finale
    with fade
    
    "The aftermath is chaotic. News crews descend on the campus. Athletes come forward with stories of coercion and experimental treatments."
    
    "Project Phoenix is exposed—a conspiracy to develop life-extension technology using college athletes as unwitting test subjects."
    
    "Jeffrey Epstein, having faked his death, is taken into custody, along with The Diddler and several university administrators."
    
    show kendrick smile at left
    with dissolve
    
    show rogan excited at center
    with dissolve
    
    show vick determined at right
    with dissolve
    
    kendrick "You did it. Your investigation blew this whole thing open."
    
    rogan "This is going to be the biggest story of the decade. Life extension technology, a supposedly dead billionaire, college sports corruption."
    
    vick "More importantly, we saved a lot of young athletes from being exploited."
    
    mc "What happens now?"
    
    show kendrick neutral
    
    kendrick "The legal battle's just beginning. These guys have powerful friends."
    
    show rogan neutral
    
    rogan "But they can't put the truth back in the box. Too many people know now."
    
    show vick smile
    
    vick "And the athletes have a chance at real reform in college sports. Maybe even fair compensation."
    
    "Your editor calls, offering you a full-time position based on your investigation."
    
    "Your story will be published nationwide."
    
    scene bg epilogue
    with fade
    
    "Six months later..."
    
    "Your exposé on Project Phoenix has won a prestigious journalism award."
    
    "College sports programs across the country are under new scrutiny and ethical oversight."
    
    "Congressional hearings have begun into the exploitation of student athletes and unethical medical research."
    
    "The trial of Jeffrey Epstein and his associates is set to begin next month."
    
    show lebron smile
    with dissolve
    
    lebron "You changed the game. Not just basketball, but how we protect young athletes."
    
    lebron "Thank you for having the courage to follow this through."
    
    hide lebron
    with dissolve
    
    if player_stats.investigation > player_stats.intellect and player_stats.investigation > player_stats.influence:
        "Your investigative instincts led you to uncover one of the biggest conspiracies in modern history."
        "You've been offered positions at major news outlets, but you're considering starting your own investigative journalism platform."
        "The Triangle Conspiracy case has made you a trusted name in uncovering truth."
        
    elif player_stats.intellect > player_stats.investigation and player_stats.intellect > player_stats.influence:
        "Your analytical approach to the conspiracy helped connect dots that others missed."
        "Academic institutions are consulting you on developing ethical oversight for sports medicine research."
        "You're writing a book about the intersection of technology, sports, and ethics that publishers are fighting to acquire."
        
    else:
        "Your connections and influence helped bring the right people together to expose the conspiracy."
        "Your social media following has exploded, giving you a platform to advocate for college athlete rights."
        "Several major athletes have asked you to help tell their stories."
    
    "Whatever path you choose next, your investigation into the Triangle Conspiracy has changed the course of your life—and protected countless others."
    
    "THE END"
    
    return