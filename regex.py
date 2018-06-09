INTRO = [
    ".*/NNP ('re|'s|'m|are|am|is)/VB.? (a|an|the)/DT .* company.*", # Copia is a non-profit company.
    ".*/NNP ('re|'s|'m|are|am|is)/VB.? (a|an|the)/DT.*", # So CNote is a high-yield savings account.
    ".*(we|it|i)/PRP.* ('re|'s|'m|are|am|is)/VB.? (a|an|the)/DT .*/NNP (of|for)/IN .*", # We are the Uber for waste-management.
    ".*(we|it|i)/PRP.* ('re|'s|'m|are|am|is)/VB.? .*/NNP.*", # We are Copia.
    ".*my/PRP.* name/NN ('s|is)/VB.*", # My name is...
    ".*(make|create|develop).*(technology|service).*",
    ".*on/IN a/DT mission/NN to.*",
    ".*mission/NN is/VB.? to.*",
    ".*goal/NN is/VB.? to.*",
    ".*disrupt.*industry.*",
    ".*revolutionize.*",
    ".*founded.*",
    "(hello|hi|hey|good.*morning|good.*day|good.*night).*",
    ".* (hello|hi|hey|good.*morning|good.*day|good.*night)/.*",
    ".*NNP.*(make|create).*",
    ".*(we|it|I)/PRP.* ('re|'s|'m|are|am|is)/VB.*/NNP.*", # We're from %company%
    ".*(we|it|I).*represent.*NNP.*", # We represent %company%
    ".*make/VB.? it/.*easy/.*for/.*",
    ".*(building|creating|developing|build|create|develop)/VB.? software/NN to/.*",
    ".*(company|startup|organisation)/NNS* (are|am|is)/VB.*/NNP", # Our company is...
    ".*(i|we)/PRP ('re|'m|are|am)/VB.? (a|an|the)/DT (co-founder|founder|partner|CEO).*NNP.*", # I'm the co-founder of Industrial/Organic.
    ".*NNP ,/, founder/NNS* (of|at)/IN .*/NNP" # %person%, founder of %org%
]

MARKET = [
    ".*enter/VB.*/DT market/NN.*",
    ".*market/NN research.*",
    ".*(?:total/JJ )?addressable/JJ market.*",
    ".*(marketing|targeting).*",
    ".*(?:target/NN )?demographic.*",
    ".*(market|marketing)/NN strategy.*",
    ".*credibility/NN in/IN the/DT market.*",
    ".*use/NN case.*",
    ".*user/NN base.*",
    ".*(niche|audience|community|age|population|segment).*",
    ".*(developing|third|first)/(NN|JJ) (world|economy).*",
    ".*work/VB.? for/.*",
    ".*market/NN need/.*",
    ".*first/JJ one/NNS?.*(introducing|introduce).*",
    ".*commercial/JJ business/.*",
    ".*(b2b|btob|business-to-business).*",
    ".*business/NN to/TO business.*",
    ".*(c2c|customer-to-customer).*",
    ".*customer/NN to/TO customer.*",
    ".*(b2g|business-to-government).*",
    ".*business/NN to/TO government.*",
    ".*(generation|millennial).*",
    ".*bread/NN and/CC butter/.*",
    "sm(e|b)/.*",
    ".* sm(e|b)/.*",
    ".*small/JJ to/TO medium/JJ sized/JJ enterprise/NN.*"
]

TEAM = [
    ".*company/NN.*started/VB.? by/IN.*NNP.*",
    ".*NNP started/VB.*company.*",
    ".*partnered/VB.? up/.*",
    ".*advisor.*",
    ".*(plan|planning)/VB.*to/TO hire/.*",
    ".*(partner|team).*",
    ".*team/NN member/.*"
]

BCKGROUND = [
    ".*background/NN is/VB.? in/IN.*",
    "worke?d?/.*company/.*",
    ".*worked/VB. as/IN .*DT.*for/IN.*year/.*"
    ".*spent/VB.? a/DT long/JJ time/NN (doing|working).*",
    ".*(working|worked).*for/IN.*for/IN the/DT (past|last)/JJ.*/CD year/.*",
    ".*started/.*career/NN at/.*",
    ".*used/VB.? to/TO be/VB.? (a|an)/DT.*",
    ".*(student|graduate|alumn..?)/NN.*",
    ".*(university|school|education|background).*",
    ".*(grew|grow|growing)/VB.? up/RP in/IN.*",
    ".*childhood.*",
    ".*for/IN.*/CD year/.*",
    ".*/CD (?:of/IN )?experience.*",
    ".*started/.*work.*in/.*",
    ".*come/VB.? from/IN.*(world|industry|background).*"
]

INVEST = [
    ".*committed/VB.? in/IN investment/.*",
    ".*seed/NN (money|round)/NN.*",
    ".*(raise|raising).*(million|thousand|hundred|dollar|buck).*",
    ".*raise/.* round/.*",
    ".*kickstarter.*",
    "valuation/.*",
    ".* valuation/.*",
    ".*(book|booked) (million|thousand|hundred|dollar|buck).*",
    ".*have/.*committed/JJ.*",
    ".*invest.*",
    ".*fundraising.*",
    ".*convertible/JJ note/NN.*"
]

FIN = [
    ".*deliver/VB.*return/NN.*",
    ".*(gross|profit)/.*margin/NN.*(?:profitable)?.*",
    ".*money/.*generate/.*",
    ".*generate/.*money/.*",
    ".*source/NN. of/IN revenue/.*",
    ".*(monetizing|monetize).*",
    ".*revenue/NN. split/.*",
    ".*/CD figure.*deal/NN.*",
    ".*(driving|drive)/VB.*cost/NN down/.*",
    ".*generat.*sale/NN.*",
    ".*presell/.*product/.*",
    ".*(revenue|business)/NN model/.*",
    ".*operation/NN. cost/NN.*",
    ".*charge/.*fee/.*",
    ".*(make|making|made|earn|bring).*money/.*",
    ".*revenue/NN run/VB.? rate/.*",
    ".*pre(?:-| )?revenue.*",
    ".*fully(-| )priced.*",
    ".*charg(e|ed|ing)/VB.*/CD.*(a|per)/(DT|IN) (second|sec|minute|min|hour|day|month|year|session).*",
    ".*(?: free/JJ)? trial/.*",
    "'*revenue/NN perspective/.*",
    ".*revenue/NN share/.*",
    ".*value/NN proposition/.*",
    ".*path/NNS? to/(IN|TO) revenue/.*"
]

IP = [
    ".* ip/.*",
    "ip/.*",
    ".*intelectual/JJ property/.*",
    ".*patent.*",
    ".*patented/JJ process/.*",
    ".*defensibility.*",
    ".*copy-?cat.*",
    ".*trademark.*"
]

COMPET = [
    ".*(i|we)/PRP ('re|'m|are|am)/VB.?(?: (a|the)/DT)? competitor/NN.? to/(TO|IN).*/NNP.*",
    ".*barrier/NN.? of/IN entry/.*",
    ".*competitor/NN.? of/IN the/DT technology/.*",
    ".*compet.*",
    ".*any.*can/.* make/VB.? this/.*",
    ".*(player|stakeholder).*"
]

PROBLEM = [
    ".*founde?d?/VB.? on/IN the/DT concept/NN.*",
    ".*thing/NN.*missing/.*",
    ".*estimated? that/.*",
    ".*(?:(technology/NN|big/JJ data/NN) )?answer/VB.? question/NN.*",
    ".*set/VB.? out/RP to/TO create/VB.*",
    ".*(have|had|having)/VB.*problem/NN.*",
    ".*('re|'s|'m|are|am|is)/VB.? (a|an|the)/DT problem/NN.? (that|which|there|here)/.*",
    ".*the/DT problem/NN.*have/.*",
    ".*the/.*problem/NN.? (that|which|there|here|is)/.*",
    ".*(our|mine|your|their)/PRP.? problem/NN.*",
    ".*been/VB.? happening/VB.? for/IN.*",
    ".*the/DT challenge/NN.? with/.*",
    ".*(realiz|issue).*",
    ".*do/VB.? (not|n't)/RB have/VB the/.*",
    ".*stem/VB.? from/IN the/DT fact/NN.*",
    ".*(this|that|there)/DT is/VB.? (a|an|the)/DT problem/NN.*",
    ".*?"
]

SOLUTION = [
    ".*(app|service|web-?site)/NN.? allow/VB.*", # our app allows you to
    ".*(?:better/JJ.? )?solution/NN.*",
    ".*(mission|goal)/NN.? of/IN the/DT (company|project|service).*",
    ".*use/VB.*to/TO.*",
    ".*designe?d?.*to/TO help/.*",
    ".*introduc(e|ing|ed)/VB.? the/DT idea/NN of/.*",
    ".*solv(e|ing|ed)/VB.? (the|this|that)/DT problem/NN.*",
    ".*address(ing|ed)/VB.*issue.*",
    ".*allow.* to/.*",
    ".*the/DT way/NN.*solv(e|ing|ed).*",
    ".*(allow|enable|available).*",
    ".*the/DT answer/NN is/.*",
    ".*(?:try)?.* to/TO help/.*"
]

TOPICS = {'Introduction': INTRO, 'Market': MARKET, 'Team': TEAM, 'Background': BCKGROUND, 'Investments': INVEST, 'Financial questions': FIN, 'Intelectual property': IP, 'Competition': COMPET, 'Problem': PROBLEM, 'Solution': SOLUTION}
