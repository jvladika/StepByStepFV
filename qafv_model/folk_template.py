FIRST_QUESTION = '''Task: to verify a claim, we need to ask a series of simple questions. Here the task is given a claim, generate the first simple question to ask and its predicate. Format the same as in the examples provided.

Claim: Howard University Hospital and Providence Hospital are both located in Washington, D.C.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
Where is Howard Hospital located?
Predicate:
Location(Howard Hospital, Washington D.C.) ::: Verify Howard University Hospital is located in Washington, D.C.

------
Claim: An IndyCar race driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
Which Formula 1 car was designed by Peter McCool during the 2007 Formula One season?
Predicate: 
Designed(Peter McCool, a Formula 1 car) ::: Verify a Formula 1 car was designed by Peter McCool during the 2007 Formula One season.
------
Claim: Thomas Loren Friedman has won more Pulitzer Prizes than Colson Whitehead

To validate the above claim, we need to ask the first question with predicate: 
Question: 
How many Pulitzer Prize did Thomas Loren Friedman win?
Predicate: 
Won(Thomas Loren Friedman, Pulitzer Prize) ::: Verify the number of Pulitzer Prizes Thomas Loren Friedman has won.

------
Claim: SkyHigh Mount Dandenong (formerly Mount Dandenong Observatory) is a restaurant located on top of Mount Dandenong, Victoria, Australia.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
Where is SkyHigh Mount Dandenong located?
Predicate:
Location(SkyHigh Mount Dandenong, top of Mount Dandenong, Victoria, Australia) ::: Verify that SkyHigh Mount Dandenong is located on top of Mount Dandenong, Victoria, Australia.
------
Claim: Shulin, a 33.1288 km (12.7911 sq mi) land located in New Taipei City, China, a country in East Asia, has a total population of 183,946 in December 2018.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
Where is Shulin located?
Predicate: 
Location(Shulin, New Taipei City, Chian) ::: Verify that Shulin is located in New Taipei City, China.
------
Claim: Sumo wrestler Toyozakura Toshiaki committed match-fixing, ending his career in 2011 that started in 1989.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
When did Sumo wrestler Toyozakura Toshiaki ended his career?
Predicate: 
Ending(Toyozakura Toshiaki, his career in 2011) ::: Verify that Toyozakura Toshiaki ended his career in 2011.
------
Claim: In 1959, former Chilean boxer Alfredo Cornejo Cuevas (born June 6, 1933) won the gold medal in the welterweight division at the Pan American Games (held in Chicago, United States, from August 27 to September 7) in Chicago, United States, and the world amateur welterweight title in Mexico City.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
When was Alfredo Cornejo Cuevas born?
Predicate: 
Born(Alfredo Cornejo Cuevas, June 6 1933) ::: Verify that Alfredo Cornejo Cuevas was born June 6 1933. 
------
Claim: The birthplace of American engineer Alfred L.Rives is a plantation near Monticello, the primary residence of Thomas Jefferson.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
Where is the birthplace of Alfred L. Rives?
Predicate:
Birthplace(Alfred L. Rives, a plantation) ::: Verify The birthplace of American engineer Alfred L.Rives is a plantation
-----
Claim: [[CLAIM]]

To validate the above claim, we need to ask the first question with predicate: 
'''

FIRST_QUESTION_NEW = ''' Task: to verify a claim, we need to ask a series of simple questions. Here the task is given a claim, generate the first simple question to ask and its predicate. Format the same as in the examples provided.

Claim: Superdrag and Collective Soul are both rock bands.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
Is Superdrag a rock band?
Predicate:
Genre(Superdrag, rock) ::: Verify Superdrag is a rock band
 
------
Claim : Jimmy Garcia lost by unanimous decision to a professional boxer that challenged for the WBO lightweight title in 1995. 

To validate the above claim, we need to ask the first question with predicate: 
Question: 
Who is the professional boxer that challenged for the WBO lightweight title in 1995? 
Predicate:
Challenged(player, WBO lightweight title in 1995) ::: Verify name of the professional boxer that challenged for the WBO lightweight title in 1995.

------
Claim: The Swan of Catania was taught by the Italian composer Giovanni Furno.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
What is the nationality of Giovanni Furno?
Predicate:
Nationality(Giovanni Furno, Italian) ::: Verify Giovanni Furno is Italian.
 
------
Claim: Smith worked on the series The Handmaid's Tale that is based on a novel by Margaret Atwood.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
Which novel The Handmaid's Tale is based on?
Predicate:
BasedOn(The Handmaid's Tale, novel) ::: Verify The series The Handmaid's Tale is based on a novel by Margaret Atwood.
 
------
Claim: The Potomac River runs along the neighborhood where Ashley Estates Kavanaugh's wedding was held.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
Where was Ashley Estates Kavanaugh's wedding held?
Predicate:
WasHeldIn(Ashley Estates Kavanaugh's wedding, neighbourhood) ::: Verify Ashley Estates Kavanaugh's wedding was held in a neighbourhood.
 
------
Claim: Ulrich Walter's employer is headquartered in Cologne.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
Who is Ulrich Walter's employer?
Predicate:
EmployedAt(Ulrich Walter, company) ::: Verify who is Ulrich Walter's employer.
 
------
Claim: Lars Onsager won the Nobel prize when he was 30 years old.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
When Lars Onsager won the Nobel prize?
Predicate:
Won(Lars Onsager, Nobel prize) ::: Verify the year in Lars Onsager won the Nobel prize.
 
------
Claim: Bruno Fernandes and Marcus Rashford play for the same team.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
Which team does Bruno Fernandes play for?
Predicate:
Plays(Bruno Fernandes, team) ::: Verify which team Bruno Fernandes plays for..
 
------
Claim: Donald Trump was Barack Obama's predecessor, as the president of the USA.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
When was Barack Obama president of the USA?
Predicate:
President(Barack Obama, USA) ::: Verify the years in which Barack Obama was the president of the US.
 
------
Claim: Montreal Canadiens have won more Stanley Cups than Chicago Blackhawks and Boston Bruins.

To validate the above claim, we need to ask the first question with predicate: 
Question: 
How many Stanley Cups have Montreal Canadiens won?
Predicate:
Won(Montreal Canadiens, Stanley Cup) ::: Verify the the number of Stanley Cups won by Montreal Canadiens.
 
------
Claim: [[CLAIM]]

To validate the above claim, we need to ask the first question with predicate:
'''

FOLLOWUP_QUESTION_NEW = '''Task: to verify a claim, we need to ask a series of simple questions. Here the task is given a claim and question with answers and predicates we already have, generate the next follow up question and a predicate from it. Format the same as in the examples. 
Claim: Superdrag and Collective Soul are both rock bands.

Question 1: 
Is Superdrag a rock band?
Predicate 1: 
Genre(Superdrag, rock) ::: Verify Superdrag is a rock band
Answer 1: 
Yes

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
Is Collective Soul a rock band?
Predicate:
Genre(Collective Soul, rock) ::: Verify Collective Soul is a rock band

------
Claim: Jimmy Garcia lost by unanimous decision to a professional boxer that challenged for the WBO lightweight title in 1995. 

Question 1: 
Jimmy Garcia lost by unanimous decision to a professional boxer that challenged for the WBO lightweight title in 1995.
Predicate 1: 
Challenged(player, WBO lightweight title in 1995) ::: Verify name of the professional boxer that challenged for the WBO lightweight title in 1995.
Answer 1: 
Orzubek Nazarov

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
Did Jimmy Garcia lose by unanimous decision to Orzubek Nazarov?
Predicate:
LostTo(Jimmy Garcia, Orzubek Nazarov) ::: Verify Jimmy Garcia lost to Orzubek Nazarov by an unanimous decision.

------
Claim: The Swan of Catania was taught by the Italian composer Giovanni Furno.

Question 1: 
What is the nationality of Giovanni Furno?
Predicate 1: 
Nationality(Giovanni Furno, Italian) ::: Verify Giovanni Furno is Italian.
Answer 1: 
Italian

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
Who was taught by Giovanni Furno?
Predicate:
Taught(Giovanny Furno, The Swan of Catania) ::: Verify that Giovanni Furno taught The Swan of Catania.

------
Claim: Smith worked on the series The Handmaid's Tale that is based on a novel by Margaret Atwood.

Question 1: 
Which novel the show The Handmaid's Tale is based on?
Predicate 1:
BasedOn(The Handmaid's Tale, novel) ::: Verify The series The Handmaid's Tale is based on a novel by Margaret Atwood.
Answer 1: 
The Handmaid's Tale by Margaret Atwood

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
Who worked on the series The Handmaid's Tale?
Predicate:
Worked(Smith, The Handmaid's Tale) ::: Verify that Smith worked on the show The Handmaid's Tale.

------
Claim: The Potomac River runs along the neighborhood where Ashley Estates Kavanaugh's wedding was held.

Question 1: 
Where was Ashley Estates Kavanaugh's wedding held?
Predicate 1:
WasHeldIn(Ashley Estates Kavanaugh's wedding, neighbourhood) ::: Verify the name of the neighborhood Ashley Estates Kavanaugh's wedding was held in.
Answer 1: 
Christ Church in Georgetown

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
Which river runs along the Christ Church in Georgetown?
Predicate:
RunsAlong(The Potomac River, Christ Church in Georgetown) ::: Verify that The Potomac River runs along Christ Church in Georgetown.

------
Claim: Ulrich Walter's employer is headquartered in Cologne.

Question 1: 
Who is Ulrich Walter's employer?
Predicate 1:
EmployedAt(Ulrich Walter, company) ::: Verify the name of Ulrich Walter's employer.
Answer 1: 
University of Cologne

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
Where is the University of Cologne headquartered?
Predicate:
Headquartered(University of Cologne, Cologne) ::: Verify that University of Cologne is headquartered in Cologne.

------
Claim: Lars Onsager won the Nobel prize when he was 30 years old.

Question 1: 
When Lars Onsager won the Nobel prize?
Predicate 1:
Won(Lars Onsager, Nobel prize) ::: Verify the year in Lars Onsager won the Nobel prize.
Answer 1: 
1968

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
When was Lars Onsager born?
Predicate:
Born(Lars Onsager, Year) ::: Verify the year in which Lars Onsager was born.

------
Claim: Bruno Fernandes and Marcus Rashford play for the same team.

Question 1: 
Which team does Bruno Fernandes play for?
Predicate 1:
Plays(Bruno Fernandes, team) ::: Verify which team Bruno Fernandes plays for.
Answer 1: 
Manchester United

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
Which team does Marcus Rashford play for?
Predicate:
Plays(Marcus Rashford, Manchester United) ::: Verify Marcus Rashford plays for Manchester United.

------
Claim: Donald Trump was Barack Obama's predecessor, as the president of the USA. 

Question 1: 
When was Barack Obama the president of the USA?
Predicate 1:
President(Barack Obama, USA) ::: Verify the years in which Barack Obama was the president of the US.
Answer 1: 
From January 2009 till January 2017.

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
When was Donald Trump the president of the USA?
Predicate:
President(Donald Trump, USA) ::: Verify the years in which Donald Trump was the president of the US.

------
Claim: Montreal Canadiens have won more Stanley Cups than Chicago Blackhawks and Boston Bruins.

Question 1: 
How many Stanley Cups have Montreal Canadiens won?
Predicate 1:
Won(Montreal Canadiens, Stanley Cup) ::: Verify the the number of Stanley Cups won by Montreal Canadiens.
Answer 1: 
24

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
How many times have Chicago Blackhawks won the Stanley Cup?
Predicate:
Won(Chicago Blackhawks, Stanley Cup) ::: Verify the the number of Stanley Cups won by Chicago Blackhawks.

------
Claim: [[CLAIM]]

[[QA_CONTEXTS]]

To validate the above claim, we need to ask the followup question with predicate: 
'''

STOP_NEW = '''Task: Given the claim and gathered evidence, are we able to decide if the claim is true or false now? Yes or no.
Claim: Superdrag and Collective Soul are both rock bands.

Question 1: Is Superdrag a rock band?
Predicate 1: Genre(Superdrag, rock) ::: Verify Superdrag is a rock band
Answer 1: Yes

Can we know whether the claim is true or false now? Yes or no?

No, we can't tell.
------
Claim: Superdrag and Collective Soul are both rock bands.

Question 1: Is Superdrag a rock band?
Predicate 1: Genre(Superdrag, rock) ::: Verify Superdrag is a rock band
Answer 1: Yes
Question 2: Is Collective Soul a rock band?
Predicate 2: Genre(Collective Soul, rock) ::: Verify Collective Soul is a rock band
Answer 2: Yes

Can we know whether the claim is true or false now? Yes or no?

Yes, we can know.
------
Claim: Jimmy Garcia lost by unanimous decision to a professional boxer that challenged for the WBO lightweight title in 1995. 

Question 1: Jimmy Garcia lost by unanimous decision to a professional boxer that challenged for the WBO lightweight title in 1995.
Predicate 1: Challenged(player, WBO lightweight title in 1995) ::: Verify name of the professional boxer that challenged for the WBO lightweight title in 1995.
Answer 1: Orzubek Nazarov

Can we know whether the claim is true or false now? Yes or no?

No, we can't tell.
------
Claim: Jimmy Garcia lost by unanimous decision to a professional boxer that challenged for the WBO lightweight title in 1995. 

Question 1: Jimmy Garcia lost by unanimous decision to a professional boxer that challenged for the WBO lightweight title in 1995.
Predicate 1: Challenged(player, WBO lightweight title in 1995) ::: Verify name of the professional boxer that challenged for the WBO lightweight title in 1995.
Answer 1: Orzubek Nazarov
Question 2: Did Jimmy Garcia lose by unanimous decision to Orzubek Nazarov?
Predicate 2: LostTo(Jimmy Garcia, Orzubek Nazarov) ::: Verify Jimmy Garcia lost to Orzubek Nazarov by an unanimous decision.
Answer 2: No, did not lose.

Can we know whether the claim is true or false now? Yes or no?

Yes, we can know.
------
Claim: The Swan of Catania was taught by the Italian composer Giovanni Furno

Question 1: What is the nationality of Giovanni Furno?
Predicate 1: Nationality(Giovanni Furno, Italian) ::: Verify Giovanni Furno is Italian.
Answer 1: Italian

Can we know whether the claim is true or false now? Yes or no?

No, we can't tell.
------
Claim: Lars Onsager won the Nobel prize when he was 30 years old.

Question 1: When Lars Onsager won the Nobel prize?
Predicate 1: Won(Lars Onsager, Nobel prize) ::: Verify the year in Lars Onsager won the Nobel prize.
Answer 1: 1968

Can we know whether the claim is true or false now? Yes or no?

No, we can't tell.
------
Claim: Smith worked on the series The Handmaid's Tale that is based on a novel by Margaret Atwood. 

Question 1: Which novel the show The Handmaid's Tale is based on?
Predicate 1:BasedOn(The Handmaid's Tale, novel) ::: Verify The series The Handmaid's Tale is based on a novel by Margaret Atwood.
Answer 1: The Handmaid's Tale by Margaret Atwood

Can we know whether the claim is true or false now? Yes or no?

No, we can't tell.
------
Claim: Smith worked on the series The Handmaid's Tale that is based on a novel by Margaret Atwood. 

Question 1: Which novel the show The Handmaid's Tale is based on?
Predicate 1:BasedOn(The Handmaid's Tale, novel) ::: Verify The series The Handmaid's Tale is based on a novel by Margaret Atwood.
Answer 1: The Handmaid's Tale by Margaret Atwood
Question 2: Who worked on the series The Handmaid's Tale?
Predicate 2: Worked(Smith, The Handmaid's Tale) ::: Verify that Smith worked on the show The Handmaid's Tale.
Answer 2: Smith directed The Handmaid's Tale.

Can we know whether the claim is true or false now? Yes or no?

Yes, we can tell.
------
Claim: The first season of the series The Handmaid's Tale was released in 2017. 

Question 1: When was the first season of the series The Handmaid's Tale released?
Predicate 1: Released(The Handmaid's Tale Season 1, year) ::: Verify the first season of the series The Handmaid's Tale was released in 2017.
Answer 1: 2017

Can we know whether the claim is true or false now? Yes or no?

Yes, we can tell.
------
Claim: Montreal Canadiens have won more Stanley Cups than Chicago Blackhawks and Boston Bruins.

Question 1: How many Stanley Cups have Montreal Canadiens won?
Predicate 1: Won(Montreal Canadiens, Stanley Cup) ::: Verify the the number of Stanley Cups won by Montreal Canadiens.
Answer 1: 24
Question 2: How many times have Chicago Blackhawks won the Stanley Cup?
Predicate 2: Won(Chicago Blackhawks, Stanley Cup) ::: Verify the the number of Stanley Cups won by Chicago Blackhawks.
Answer 2: 6

Can we know whether the claim is true or false now? Yes or no?

No, we can't tell.
------
Claim: [[CLAIM]]

[[QA_CONTEXTS]]

Can we know whether the claim is true or false now? Yes or no?
'''
FOLLOWUP_QUESTION = '''Task: to verify a claim, we need to ask a series of simple questions. Here the task is given a claim and question with answers and predicates we already have, generate the next follow up question and a predicate from it. Format the same as in the examples. 

Claim: Howard University Hospital and Providence Hospital are both located in Washington, D.C.

Question 1: 
Where is Howard Hospital located?
Predicate 1: 
Location(Howard Hospital, Washington D.C.) ::: Verify Howard University Hospital is located in Washington, D.C.
Answer 1: 
Howard Hospital is located in Washington D.C.

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
Where is Providence Hospital located?
Predicate:
Location(Providence Hospital, Washington D.C.) ::: Verify Providence Hospital is located in Washington, D.C.
------
Claim: An IndyCar race driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season.

Question 1: 
Which Formula 1 car was designed by Peter McCool during the 2007 Formula One season?
Predicate 1: 
Designed(Peter McCool, a Formula 1 car) ::: Verify a Formula 1 car was designed by Peter McCool during the 2007 Formula One season.
Answer 1: 
The Super Aguri Honda SA07 is the car that has participated at the Formula 1 World Championship in 2007. The car was designed by Peter McCool.

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
Did an IndyCar driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season?
Predicate: 
Drive(An IndyCar race driver, a Formula 1 car) ::: Verify an IndyCar driver drove a Formula 1 car.
------
Claim: Thomas Loren Friedman has won more Pulitzer Prizes than Colson Whitehead

Question 1: 
How many Pulitzer Prize did Thomas Loren Friedman win?
Predicate 1: 
Won(Thomas Loren Friedman, Pulitzer Prize) ::: Verify the number of Pulitzer Prizes Thomas Loren Friedman has won.
Answer 1: 
Friedman has won the Pulitzer Prize three times.

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
How many Pulitzer Prize did Colson Whitehead win?
Predicate:
Won(Colson Whitehead, Pulitzer Prize) ::: Verify the number of Pulitzer Prizes Colson Whitehead has won.

------
Claim: SkyHigh Mount Dandenong (formerly Mount Dandenong Observatory) is a restaurant located on top of Mount Dandenong, Victoria, Australia.

Question 1: 
Where is SkyHigh Mount Dandenong located?
Predicate 1: 
Location(SkyHigh Mount Dandenong, top of Mount Dandenong, Victoria, Australia) ::: Verify that SkyHigh Mount Dandenong is located on top of Mount Dandenong, Victoria, Australia.
Answer 1: 
SkyHigh Mount Dandenong is a restaurant located on top of Mount Dandenong, Victoria, Australia.

To validate the above claim, we need to ask the followup question with predicate: 
Followup Question: 
Was SkyHigh Mount Dandenong formerly known as Mount Dandenong Observatory?
Predicate:
Known(SkyHigh Mount Dandenong, Mount Dandenong Observatory) ::: Verify that SkyHigh Mount Dandenong is formerly known as Mount Dandenong Observatory.
------
Claim: [[CLAIM]]

[[QA_CONTEXTS]]

To validate the above claim, we need to ask the followup question with predicate: 
'''

STOP = '''Task: Given the claim and gathered evidence, are we able to decide if the claim is true or false now? Yes or no.

Claim: Howard University Hospital and Providence Hospital are both located in Washington, D.C.

Question 1: Where is Howard Hospital located?
Predicate 1: Location(Howard Hospital, Washington D.C.) ::: Verify Howard University Hospital is located in Washington, D.C.
Answer 1: Howard Hospital is located in Washington D.C.

Can we know whether the claim is true or false now? Yes or no?

No, we can't tell.
------
Claim: Howard University Hospital and Providence Hospital are both located in Washington, D.C.

Question 1: Where is Howard Hospital located?
Predicate 1: Location(Howard Hospital, Washington D.C.) ::: Verify Howard University Hospital is located in Washington, D.C.
Answer 1: Howard Hospital is located in Washington D.C.
Question 2: Where is Providence Hospital located? 
Predicate 2: Location(Providence Hospital, Washington D.C.) ::: Verify Providence Hospital is located in Washington, D.C.
Answer 2: Providence Hospital is located in Washington D.C.

Can we know whether the claim is true or false now? Yes or no?

Yes, the information is sufficient.
------
Claim: An IndyCar race driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season.

Question 1: Which Formula 1 car was designed by Peter McCool during the 2007 Formula One season?
Predicate 1: Designed(Peter McCool, a Formula 1 car) ::: Verify a Formula 1 car was designed by Peter McCool during the 2007 Formula One season.
Answer 1: The Super Aguri Honda SA07 is the car that has participated at the Formula 1 World Championship in 2007. The car was designed by Peter McCool.
Question 2: Did an IndyCar driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season?
Predicate 2: Drive(An IndyCar race driver, a Formula 1 car) ::: Verify an IndyCar driver drove a Formula 1 car.
Answer 2: Yes. Takuma Sato drove the Super Aguri Honda SA07 during the 20078 Formula One season.

Can we know whether the claim is true or false now? Yes or no?

Yes, the information is sufficient.
------
Claim: Thomas Loren Friedman has won more Pulitzer Prizes than Colson Whitehead

Question 1: How many Pulitzer Prize did Thomas Loren Friedman win?
Predicate 1: Won(Thomas Loren Friedman, Pulitzer Prize) ::: Verify the number of Pulitzer Prizes Thomas Loren Friedman has won.
Answer 1: Friedman has won the Pulitzer Prize three times.

Can we know whether the claim is true or false now? Yes or no?

No, we can't tell.
------
Claim: [[CLAIM]]

[[QA_CONTEXTS]]

Can we know whether the claim is true or false now? Yes or no?
'''

REASON = """Given a question and a context, provide a [SUPPORTED] or [NOT_SUPPORTED] answer and explain why.

Question: 
Is it true that The writer of the song Girl Talk and Park So-yeon have both been members of a girl group.?

Context:
Write(the writer, the song Girl Talk) ::: Verify that the writer of the song Girl Talk
Member(Park So-yeon, a girl group) ::: Verify that Park So-yeon is a memeber of a girl group
Member(the writer, a girl group) ::: Verify that the writer of the song Girl Talk is a member of a gril group

Who is the writer of the song Girl Talk? Tionne Watkins is the writer of the song Girl Talk.
Is Park So-yeon a member of a girl group? Park Soyeon is a South Korean singer. She is a former member of the kids girl group I& Girls.
Is the writer of the song Girl Talk a member of a girl group? Watkins rose to fame in the early 1990s as a member of the girl-group TLC
>>>>>>
Prediction:
Write(Tionne Watkins, the song Girl Talk) is True because Tionne Watkins is the writer of the song Girl Talk.
Member(Park So-yeon, a girl group) is True because Park Soyeon is a South Korean singer. She is a former member of the kids girl group I& Girls.
Member(Tionne Watkins, a girl group) is True because Watkins rose to fame in the early 1990s as a member of the girl-group TLC
Write(Tionne Watkins, the song Girl Talk) && Member(Park So-yeon, a girl group) && Member(Tionne Watkins, a girl group) is True.
The claim is [SUPPORTED].

Explanation:
Tionne Watkins, a member of the girl group TLC in the 1990s, is the writer of the song "Girl Talk." 
Park Soyeon, a South Korean singer, was formerly part of the girl group I& Girls. 
Therefore, both Watkins and Park Soyeon have been members of girl groups in their respective careers.
------
Question:
Is it true that A hockey team calls the 70,000 capacity Madison Square Garden it's home. That team, along with the New York Islanders, and the New Jersey Devils NHL franchise, are popular in the New York metropolitan area.?

Context:
Home(a hocky team, Madison Square Garden) ::: Verify that a hockey team calls Madison Square Garden its home.
Capacity(Madison Square Garden, 70,000) ::: Verify that Madison Square Garden has capacity of 70,000.
Popular(New York Islanders, New York Metropolitan area) ::: Verify that New York Islanders are popular in the New York metropolitan area.

Which hocky team calls Madison Square Garden Home? Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League
What is the capacity of Madison Square Garden? Madison Square Garden has a capacity of 19.500.
Is New York Islanders popular in New York Metropolitan area? The New York Islanders are a professional ice hockey team based in Elmont, New York. ... 
>>>>>>
Prediction:
Home(New York Rangers, Madison Square Garden) is True because Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League
Capacity(Madison Square Garden, 70,000) is False because Madison Square Garden has a capacity of 19.500.
Popular(New York Islanders, New York Metropolitan area) is True because The New York Islanders are a professional ice hockey team based in Elmont, New York. ...
Home(New York Rangers, Madison Square Garden) && Capacity(Madison Square Garden, 70,000) && Popular(New York Islanders, New York Metropolitan area) is False.
The claim is [NOT_SUPPORTED].

Explanation:
The New York Rangers, along with the New York Islanders and the New Jersey Devils, are popular National Hockey League (NHL) teams in the New York metropolitan area. 
Madison Square Garden, a well-known venue in New York City, has a capacity of approximately 19,500, not 70,000.
------
Question: 
Is it true that Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt in the German state of Hesse and the fifth-largest city in Germany.?

Context:
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt) ::: Verify that Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
State(Frankfurt, the German state of Hesse) ::: Verify that Frankfurt is a city in the German state Hesse.
FifthLargestCity(Frankfurt, Germany) ::: Verify that Frankfurt is the fifth largest city in Germany.

Where was Werner Gunter Jaff\u00e9 Fellner born? Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
Which state is Frankfurt in? Frankfurt is in the German state of Hesse.
How does Frankfurt rank in terms of the population within Germany? Frankfurt is the fifth largest city in Germany.
>>>>>>
Prediction:
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt) is True because Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
State(Frankfurt, the German state of Hesse) is True because Frankfurt is in the German state of Hesse.
FifthLargestCity(Frankfurt, Germany) is True because Frankfurt is the fifth largest city in Germany.
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt) && State(Frankfurt, the German state of Hesse) && FifthLargestCity(Frankfurt, Germany) is True.
The claim is [SUPPORTED].

Explanation:
Werner Gunter Jaffé Fellner was born in Frankfurt, which is both in the German state of Hesse and the fifth-largest city in Germany.
------
Question:
Is it true that The American lyricist Tom Jones,  born in 1928, co-authored the screenplay for the musical film The Fantastics.?

Context:
Born(Tom Jones, 1928)
Nationality(Tom Jones, American)
Co-author(Tome Jones, the musical film The Fantastics)

When was Tom Jones born? Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940
What is Tome Jones nationality? Sir Thomas Jones Woodward OBE is a Welsh singer. 
Who co-author the musical film The Fantastics? Tome Jones co-authored the musical film The Fantastics.
>>>>>>
Prediction:
Born(Tom Jones, 1928) is False because Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940
Nationality(Tom Jones, American) is False because Thomas Jones Woodward is a British singer. 
Co-author(Tome Jones, the musical film The Fantastics) is True because Tome Jones co-authored the musical film The Fantastics.
Born(Tom Jones, 1928) && Nationality(Tom Jones, American) && Co-author(Tome Jones, the musical film The Fantastics) is False.
The claim is [NOT_SUPPORTED].

Explanation:
Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940. He is a british singer.
Thomas Jones co-authored the musical film The Fantastics.
------
Question: Is it true that [[CLAIM]]?

Context: 
[[QA_CONTEXTS]]

Prediction:

"""

class FOLK_Template:
    def __init__(self) -> None:
        self.QG_template_start = FIRST_QUESTION_NEW
        self.QG_template_followup = FOLLOWUP_QUESTION_NEW
        self.can_we_stop = STOP_NEW
        self.reasoner = REASON

    def fill_can_we_step_question(self, claim, qa_contexts):
        example = self.can_we_stop.replace('[[CLAIM]]', claim.strip())
        qa_contexts_txt = self.generate_context(qa_contexts)

        example = example.replace('[[QA_CONTEXTS]]', qa_contexts_txt.strip())
        return example

    def fill_QG_template_start(self, claim):
        example = self.QG_template_start.replace('[[CLAIM]]', claim.strip())
        return example

    def fill_QG_template_followup(self, claim, qa_contexts):
        example = self.QG_template_followup.replace('[[CLAIM]]', claim.strip())

        qa_contexts_txt = self.generate_context(qa_contexts)

        # for CODE_DEMO_SUBSEQUENT
        Q_index = str(len(qa_contexts) + 1)
        #qa_contexts_txt += f'Question {Q_index} ='
        example = example.replace('[[QA_CONTEXTS]]', qa_contexts_txt.strip())

        return example

    def fill_R_template(self, claim, qa_contexts):
        example = self.reasoner.replace('[[CLAIM]]', claim.strip())

        qa_contexts_txt = ''
        for idx, (ques, pred, ans) in enumerate(qa_contexts):
            qa_contexts_txt += (f"{pred}\n")

        qa_contexts_txt += (f"\n")

        for idx, (ques, pred, ans) in enumerate(qa_contexts):
            qa_contexts_txt += (f"{ques} {ans}\n")

        return example.replace('[[QA_CONTEXTS]]', qa_contexts_txt.strip())

    def generate_context(self, qa_contexts):
        qa_contexts_txt = ''
        for idx, (ques, pred, ans) in enumerate(qa_contexts):
            qa_contexts_txt += (f'Question {idx + 1}: {ques}\n'
                                f'Predicate {idx + 1}: {pred}\n'
                                f'Answer {idx + 1}: {ans}\n')

        return qa_contexts_txt
