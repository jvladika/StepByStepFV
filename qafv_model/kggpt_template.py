FIRST_QUESTION_NEW = """
Task: to verify a claim, we need to ask a series of simple questions. Here the task is given a claim, generate the first question to ask. This question should be simple enough with a single subject-predicate-object structure.

Claim = Ahmad Kadhim Assad's club is Al-Zawra'a SC.
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Is Ahmad Kadhim Assad's club Al-Zawra'a SC?

Claim = Yeah! I know that Bananaman, which starred Tim Brooke-Taylor, first aired on 3rd October 1983!
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Did Bananman star Tim Brooke-Taylor? 

Claim = AIDA Cruise line operated the ship which was built by Meyer Werft in Townsend, Poulshot, Wiltshire.
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Did AIDA cruise operate a ship?

Claim = Really? Jamie Lawrence is the music composer of the 83 minute 'Death on a Factory Farm' film, directed by Sarah Teale!
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Is Jamie Lawrence the music composer of 'Death on a Factory Farm' film?

Claim = Brandon Carter was born in England and graduated from the University of Cambridge where the current Chancellor is Leszek Borysiewicz.
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Was Brandon Carter born in England?

Claim = No, but the leader of the United States is not Olena Serdiuk.
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Is Olena Serdiuk the leader of the United States?

Claim = Yes, with a floor count of 45, 200 Public Square is located in Cleveland in the United States.
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Does 200 Public Square have a floor count of 45?

Claim = Bananaman the TV series starred by a person was shown on the company and the company headquarters is called Broadcasting House.
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Did Bananaman the TV series star a person?

Claim = Do you know Milan Hodža? he had a religion.
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Did Milan Hodža have a religion?

Claim = The place, designed by Huseyin Butuner and Hilmi Guner, is located in a country, where the leader is Artur Rasizade.
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Is there a place designed by Huseyin Butuner and Hilmi Guner?

Claim = An academic journal with code IJPHDE is also Acta Math. Hungar.
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Is there an academic journal with code IJPHDE?

Claim = 'A film' was produced by Anatole de Grunwald, directed by Harold French, with cinematography done by Bernard Knowles.
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Was 'A film' produced by Anatole de Grunwald?

Claim = Marcus Rashford and Bruno Fernandes play for Mancherster United.
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Does Marcus Rashford play for Manchester United?

Claim = The Nobel prize award winning writer created the book character Harry Potter.'
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question = Which writer created the book character Harry Potter?

Claim =  [[CLAIM]]
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 

"""


FOLLOWUP_QUESTION = """
Task: to verify a claim, we need to ask a series of simple questions. Here the task is given a claim and already asked questions with answers, generate the next question to ask. This question should be simple enough with a single subject-predicate-object structure.


Claim = Yeah! I know that Bananaman, which starred Tim Brooke-Taylor, first aired on 3rd October 1983!
Question 1 = Did Bananman star Tim Brooke-Taylor? 
Answer 1 = Yes, Bananman starred Tim Brooke-Taylor.
To validate the above claim, we need to ask the following next simple subject-predicate-object question: 
Question 2 = Did Bananaman first air on 3rd October 1983?

Claim = AIDA Cruise line operated the ship which was built by Meyer Werft in Townsend, Poulshot, Wiltshire.
Question 1 = Did AIDA cruise operate a ship?
Answer 2 = AIDA cruise operated a ship called Bounty.
To validate the above claim, we need to ask the following next simple subject-predicate-object question: 
Question 2 = Was ship Bounty built by Meyer Werft?

Claim = Really? Jamie Lawrence is the music composer of the 83 minute 'Death on a Factory Farm' film, directed by Sarah Teale!
Question 1 = Is Jamie Lawrence the music composer of 'Death on a Factory Farm' film?
Answer 1 = Yes, Jamie Lawrence composed music of the film called 'Death on a Factory Farm'.
To validate the above claim, we need to ask the following next simple subject-predicate-object question: 
Question 2 = Does 'Death on Factory Farm' have 83 minutes?

Claim = Brandon Carter was born in England and graduated from the University of Cambridge where the current Chancellor is Leszek Borysiewicz.
Question 1 = Was Brandon Carter born in England?
Answer 1 = Brandon Carter was born in England.
Question 2 = Did Brandond Carter graduate from the Uniiversity of Cambridge?
Answer 2 = Brandond Carter graduated from the University of Cambridge.
To validate the above claim, we need to ask the following next simple subject-predicate-object question: 
Question 3 = Is the current Chancellor of the University of Cambridge Leszek Borysiewicz?

Claim = Yes, with a floor count of 45, 200 Public Square is located in Cleveland in the United States.
Question 1 = Does 200 Public Square have a floor count of 45?
Answer 1 = 200 Public Square has 45 floors.
To validate the above claim, we need to ask the following next simple subject-predicate-object question: 
Question 2 = Is 200 Public Square in Cleveland?

Claim = Bananaman the TV series starred by a person was shown on the company and the company headquarters is called Broadcasting House.
Question 1 = Did Bananaman the TV series star a person?
Answer 1 = Yes, Bananaman starred Robert de Niro.
To validate the above claim, we need to ask the following next simple subject-predicate-object question: 
Question 2 = Was Bananaman shown at a company?


Claim = The place, designed by Huseyin Butuner and Hilmi Guner, is located in a country, where the leader is Artur Rasizade.
Question 1 = Is there a place designed by Huseyin Butuner and Hilmi Guner?
Answer 1 = Taipei 101 was designed by Huseyin Butuner and Hilmi Guner.
Question 2 = Is Taipei 101 located in a country?
Answer 2 = Taipei 101 is located in Taiwan.
To validate the above claim, we need to ask the following next simple subject-predicate-object question: 
Question 3 = Is Artur Rasizade leader of Taiwan?


Claim = 'A film' was produced by Anatole de Grunwald, directed by Harold French, with cinematography done by Bernard Knowles.
Question 1 = Was 'A film' produced by Anatole de Grunwald?
Answer 1 = Yes, 'A film' was produced by Anatole de Grunwald.
To validate the above claim, we need to ask the following next simple subject-predicate-object question: 
Question 2 = Did Harold French direct 'A film'?

Claim = The Nobel prize award winning writer created the book character Harry Potter.'
To validate the above claim, we need to ask the following first simple subject-predicate-object question: 
Question 1 = Which writer created the book character Harry Potter?
Answer 1 = JK Rowling
Question 2 = Did JK Rowling win a Nobel prize?

Claim =  [[CLAIM]]
[[QA_CONTEXTS]]
To validate the above claim, we need to ask the following next simple subject-predicate-object question: 

"""


FIRST_QUESTION = """
Task: to verify a claim, we need to ask a series of simple questions which can be represented by triplets. Here the task is given a claim and entities, generate the first simple question to ask, so we can verify the claim. The question should contain 2 entities at most. The question entity set should contain no more than two entities, with each entity being used only once.

Claim = Ahmad Kadhim Assad's club is Al-Zawra'a SC.
Entity set = ['Ahmad_Kadhim_Assad' ## "Al-Zawra'a_SC"] 
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Is Ahmad Kadhim Assad's club Al-Zawra'a SC?
Question Entity set = ['Ahmad_Kadhim_Assad' ## "Al-Zawra'a_SC"]

Claim = Yeah! I know that Bananaman, which starred Tim Brooke-Taylor, first aired on 3rd October 1983!
Entity set = ['"1983-10-03"' ## 'Tim_Brooke-Taylor' ## 'Bananaman'] 
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Did Bananman star Tim Brooke-Taylor? 
Question Entity set = ['Bananaman' ## 'Tim_Brooke-Taylor'] 

CLaim = AIDA Cruise line operated the ship which was built by Meyer Werft in Townsend, Poulshot, Wiltshire.
Entity set = ['Meyer_Werft' ## 'AIDA_Cruises' ## '"Townsend, Poulshot, Wiltshire"']
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Did AIDA cruise operate a ship?
Question Entity set = ['AIDA_Cruises' ## 'ship'] 

Claim = Really? Jamie Lawrence is the music composer of the 83 minute 'Death on a Factory Farm' film, directed by Sarah Teale!
Entity set = ['Jamie_Lawrence' ## '"83.0"' ## 'Death_on_a_Factory_Farm' ## 'Sarah_Teale'] 
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Is Jamie Lawrence the music composer of 'Death on a Factory Farm' film?
Question Entity set = ['Jamie_Lawrence' ## 'Death_on_a_Factory_Farm'] 

Claim = Brandon Carter was born in England and graduated from the University of Cambridge where the current Chancellor is Leszek Borysiewicz.
Entity set = ['Brandon_Carter' ## 'University_of_Cambridge' ## 'Leszek_Borysiewicz' ## 'England'] 
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Was Brandon Carter born in England?
Question Entity set = ['Brandon_Carter' ## 'England'] 

Claim = No, but the leader of the United States is not Olena Serdiuk.
Entity set: ['United_States' ## '"Olena Serdiuk"'] 
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Is Olena Serdiuk the leader of the United States?
Question Entity set = ['United_States' ## '"Olena Serdiuk"'] 

Claim = Yes, with a floor count of 45, 200 Public Square is located in Cleveland in the United States.
Entity set: ['200_Public_Square' ## 'Cleveland' ## 'United_States' ## '"45"']
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Does 200 Public Square have a floor count of 45?
Question Entity set = ['200_Public_Square' ## '"45"']

Claim = Bananaman the TV series starred by a person was shown on the company and the company headquarters is called Broadcasting House.
Entity set: ['Broadcasting_House' ## 'Bananaman'] 
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Did Bananaman the TV series star a person?
Question Entity set = ['Bananaman' ## 'person'] 

Claim = Do you know Milan Hodža? he had a religion.
Entity set = ['Milan_Hodža'] 
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Did Milan Hodža have a religion?
Question Entity set = ['Milan_Hodža'] 

Claim = The place, designed by Huseyin Butuner and Hilmi Guner, is located in a country, where the leader is Artur Rasizade.
Entity set = ['"Hüseyin Bütüner and Hilmi Güner"' ## 'Artur_Rasizade'] 
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Is there a place designed by Huseyin Butuner and Hilmi Guner?
Question Entity set = ['place' ## '"Hüseyin Bütüner and Hilmi Güner"']

Claim = An academic journal with code IJPHDE is also Acta Math. Hungar.
Entity set: ['"Acta Math. Hungar."' ## '"IJPHDE"']
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Is there an academic journal with code IJPHDE?
Question Entity set = ['academic journal' ## '"IJPHDE"']

Claim = 'A film' was produced by Anatole de Grunwald, directed by Harold French, with cinematography done by Bernard Knowles.
Entity set = ['Anatole_de_Grunwald' ## 'Bernard_Knowles' ## 'Harold_French'] 
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Is there a film produced by Anatole de Grunwald?
Question Entity set = ['film' ## 'Anatole_de_Grunwald'] 

Claim = Marcus Rashford and Bruno Fernandes play for Mancherster United.
Entity set = ['Marcus_Rashford', 'Bruno_Fernandes', 'Manchester_United']
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 
Question = Does Marcus Rashford play for Manchester United?
Question Entity set = ['Marcus_Rashford' ## 'Manchester_United'] 

Claim =  [[CLAIM]]
Entity set = [[ENTITIES]]
To validate the above claim, we need to ask the following first simple question with the corresponding entity set of 2 entities at most: 

"""

RELATION_RETRIEVAL_NEW = """
I will give you a set of words. 
Find the element from Words set which is most semantically related to the given question. Choose a word only from the word list. If there is nothing that looks semantically related, return [].

Question = Is Ahmad Kadhim Assad's club Al-Zawra'a SC?
Words set = ['club', 'clubs',  'leaderName', 'award', 'vicepresident', 'vicePresident'] 
Semantically most similar word from the word set to the question is: 
Answer = club


Question = Did Bananman star Tim Brooke-Taylor?
Words set = ['OwningCompany', 'owner', 'writer', 'director', 'formerTeam', 'starring'] 
Semantically most similar word from the word set to the question is: 
Answer: starring


Question = Is there a film produced by Anatole de Grunwald?
Words set = ['composer',  'starring', 'runtime', 'director',  'writer', 'producer', 'cinematography']
Semantically most similar word from the word set to the question is:  
Answer = producer


Question = Is Jamie Lawrence the music composer of 'Death on a Factory Farm' film?
Words set = ['composer', 'starring',  'director', 'founder', 'crewMembers', 'writer'] 
Semantically most similar word from the word set to the question is: 
Answer = composer


Question =  Is Olena Serdiuk the leader of the United States?
Words set = ['composer', 'team', 'president', 'editor', 'starring', 'runtime', 'director', 'discoverer', 'founder', 'crewMembers', 'writer', 'producer', 'cinematography'] 
Semantically most similar word from the word set to the question is: 
Answer = president


Question = Was Brandon Carter born in England?
Words set = ['OwningCompany', 'placeOfBirth', 'owner', 'viceChancellor', 'almaMater', 'dean', 'coach', 'writer', 'firstAired', 'director', 'formerTeam', 'starring', 'birthPlace'] 
Semantically most similar word from the word set to the question is: 
Answer = birthPlace


Question = Did AIDA Cruise line operate a ship?
Words set: ['location', 'firstAired', 'clubs', 'parent', 'network', 'shipBuilder', 'birthPlace', 'locationCity', 'shipOperator', 'leaderName', 'awards', 'vicePresident'] 
Answer: shipOperator


Question = Does 200 Public Square have 45 floors?
Words set: ['producer', 'floorCount', 'country', 'location', 'primeMinister', 'parent', 'spouse', 'nativeName', 'builder', 'manager', 'designer'] 
Answer: floorCount


Question = Did Milan Hodža have a religion?
Words set = ['deathYear', 'leaderName', 'awards', 'award'] 
Answer = []


Question = Did Huseyin Butuner design a place?
Words set: ['producer', 'primeMinister', 'parent', 'leaderName' 'spouse', 'nativeName', 'manager', 'location'] 
Answer = []



Question = [[QUESTION]]
Words set = [[RELATION_SET]]
Answer = 
"""

RELATION_RETRIEVAL = """
I will give you a set of words. 
Find the top [[TOP_K]] elements from Words set which are most semantically related to the given question. You may select up to [[TOP_K]] words. If there is nothing that looks semantically related, pick out any [[TOP_K]] elements and give them to me.

Question = Is Ahmad Kadhim Assad's club Al-Zawra'a SC?
Words set = ['club', 'clubs',  'leaderName', 'award', 'vicepresident', 'vicePresident'] 
Top 2 Answer = ['club', 'clubs']


Question = Did Bananman star Tim Brooke-Taylor?
Words set = ['OwningCompany', 'owner', 'writer', 'director', 'formerTeam', 'starring'] 
Top 1 Answer: ['starring'] 


Question = Is there a film produced by Anatole de Grunwald?
Words set = ['composer',  'starring', 'runtime', 'director',  'writer', 'producer', 'cinematography'] 
Top 3 Answer = ['producer', 'director', 'cinematography']


Question = Is Jamie Lawrence the music composer of 'Death on a Factory Farm' film?
Words set = ['composer', 'starring',  'director', 'founder', 'crewMembers', 'writer'] 
Top 2 Answer = ['composer', 'writer']


Question =  Is Olena Serdiuk the leader of the United States?
Words set = ['composer', 'team', 'president', 'editor', 'starring', 'runtime', 'director', 'discoverer', 'founder', 'leader', 'crewMembers', 'writer', 'producer', 'cinematography'] 
Top 1 Answer = ['leader', 'president']


Question = Was Brandon Carter born in England?
Words set: ['OwningCompany', 'placeOfBirth', 'owner', 'viceChancellor', 'almaMater', 'dean', 'coach', 'writer', 'firstAired', 'director', 'formerTeam', 'starring', 'birthPlace'] 
Top 2 Answer: ['birthPlace', 'placeOfBirth']


Sentence G: AIDA Cruise line operated the ship which was built by Meyer Werft in Townsend, Poulshot, Wiltshire.
Words set: ['location', 'firstAired', 'clubs', 'parent', 'network', 'shipBuilder', 'birthPlace', 'locationCity', 'shipOperator', 'leaderName', 'awards', 'award', 'vicepresident', 'vicePresident'] 
Top 4 Answer: ['shipBuilder', 'location', 'locationCity', 'shipOperator',]


Sentence H: Yes, with a floor count of 45, 200 Public Square is located in Cleveland in the United States.
Words set: ['producer', 'floorCount', 'country', 'location', 'primeMinister', 'parent', 'spouse', 'nativeName', 'builder', 'manager', 'designer'] 
Top 3 Answer: ['floorCount', 'country', 'location']


Sentence I: Bananaman the TV series starred by a person was shown on the company and the company headquarters is called Broadcasting House.
Words set: ['composer', 'team', 'editor', 'starring', 'locationCity', 'runtime', 'network', 'discoverer', 'founder', 'crewMembers', 'writer'] 
Top 3 Answer: ['locationCity', 'starring','network']


Sentence J: Do you know Milan Hodža? he had a religion.
Words set: ['deathYear', 'leaderName', 'awards', 'award', 'religion'] 
Top 1 Answer: ['religion']


Sentence K: The place, designed by Huseyin Butuner and Hilmi Guner, is located in a country, where the leader is Artur Rasizade.
Words set: ['producer', 'primeMinister', 'parent', 'leaderName' 'spouse', 'nativeName', 'builder', 'manager', 'designer', 'location'] 
Top 3 Answer: ['designer', 'leaderName', 'location']


Sentence L: An academic journal with code IJPHDE is also Acta Math. Hungar.
Words set: ['abbreviation', 'placeOfBirth', 'owner', 'coden', 'almaMater', 'dean', 'coach', 'writer', 'firstAired', 'director', 'formerTeam', 'starring', 'birthPlace'] 
Top 2 Answer: ['abbreviation', 'coden']


Now let's find the top <<<<TOP_K>>>> elements.
Sentence: <<<<SENTENCE>>>>
Words set: <<<<RELATION_SET>>>>
Top <<<<TOP_K>>>> Answer: 
"""

TRIPLE_TO_EVIDENCE = """
I will give you a set of triples. Generate a sentence from each subject-predicate-object triples in the set. 

Triple set: [(Harry Potter, successor, Ron Weasley)]
Sentence: Harry Potter has a successor named Ron Weasley.

Triple set: [(Leonardo DaVinci, deathPlace, France)]
Sentence: Leonardo Davinci's place of death is France.


Triple set: [(Leonardo DiCaprio, starring, Catch Me If You Can), (Leonardo DiCaprio, starring, Titanic)]
Sentence: Leonardo DiCaprio starred in Catch Me If You Can and Titanic.

Triple set: [[TRIPLES]]
Sentence:
"""


class KGGPT_Template:
    def __init__(self) -> None:
        self.QG_template_start = FIRST_QUESTION_NEW
        self.RR_template = RELATION_RETRIEVAL_NEW
        self.QG_template_followup = FOLLOWUP_QUESTION
        self.triples_to_sentence_template = TRIPLE_TO_EVIDENCE
        #self.can_we_stop = CODE_DEMO_STOP

    """
    def fill_can_we_step_question(self, claim, qa_contexts):
        example = self.can_we_stop.replace('[[CLAIM]]', claim.strip())
        qa_contexts_txt = ''
        for idx, (ques, ans) in enumerate(qa_contexts):
            qa_contexts_txt += f'Question {idx + 1} = {ques}\nAnswer {idx + 1} = {ans}\n'
        example = example.replace('[[QA_CONTEXTS]]', qa_contexts_txt.strip())
        return example
        """

    def fill_QG_template_start(self, claim):
        example = self.QG_template_start.replace('[[CLAIM]]', claim.strip())

        return example

    def fill_RR_template(self, question, relations):
        example = self.RR_template.replace('[[QUESTION]]', question).replace('[[RELATION_SET]]', str(relations)).strip()

        return example


    def fill_QG_template_followup(self, claim, qa_contexts):
        example = self.QG_template_followup.replace('[[CLAIM]]', claim.strip())

        qa_contexts_txt = ''
        for idx, (ques, ans) in enumerate(qa_contexts):
            qa_contexts_txt += f'Question {idx + 1} = {ques}\nAnswer {idx + 1} = {ans}\n'

        ## for CODE_DEMO_SUBSEQUENT
        Q_index = str(len(qa_contexts) + 1)
        qa_contexts_txt += f'Question {Q_index} ='
        example = example.replace('[[QA_CONTEXTS]]', qa_contexts_txt.strip())

        return example


    def fill_triples_to_sentence_template(self, triples):
        example = self.triples_to_sentence_template.replace('[[TRIPLES]]', str(triples))

        return example
