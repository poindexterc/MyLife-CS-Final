from urllib import *
from xml.dom import minidom
import re

class myLife:
    def __init__(self):
        liIndex = 0
        firstTime = input('Hello! Is this the first time you have started your life? ')
        firstTime = firstTime.lower()
        if firstTime == 'yes':
            file = open('myLifePrefs', 'w')

            name = input('Ok then, whats your name? ')
            favTeam = input('Great! Whats your favorite sports team? ')
            favArtist = input('Ok, who is your favorite artist? ')
            favTwit = input('Excellent! Who is your favorite twitter personality? ')
            location = input('Almost Done! Now, all I need is your current zip code: ')
            info = name + ' \n' + favTeam+ ' \n' + favArtist+ ' \n' + favTwit+ ' \n' +location
            print('///CREATING YOUR LIFE/// \n')
            file.write(str(info))
            print('///LIFE CREATED/// \n')
            file.close()
            prefsFile = open('myLifePrefs', 'r')
            for line in prefsFile:
                liIndex = liIndex + 1
                l = line.replace('\n', '')
                if liIndex == 1:
                    self.name = l
                elif liIndex == 2:
                    self.favTeam = l
                elif liIndex == 3:
                    self.favArtist = l
                elif liIndex == 4:
                    self.favTwit = l
                elif liIndex == 5:
                    self.location = l
            learning = open('myLifeLearning', 'w')
            learning.close() 
            
            print('///LOADING YOUR LIFE/// \n')
            self.welcome(self.getName())
   
            
        else:
            print('///LOADING YOUR LIFE/// \n')
            prefsFile = open('myLifePrefs', 'r')
            
            for line in prefsFile:
                liIndex = liIndex + 1
                l = line.replace('\n', '')
                if liIndex == 1:
                    self.name = l
                elif liIndex == 2:
                    self.favTeam = l
                elif liIndex == 3:
                    self.favArtist = l
                elif liIndex == 4:
                    self.favTwit = l
                elif liIndex == 5:
                    self.location = l
            learning = open('myLifeLearning', 'a')
            learning.close()
            self.prefsFile = prefsFile
            self.welcome(self.getName())

    def getName(self):
        return self.name

    def getFavTeam(self):
        return self.favTeam

    def getFavArtist(self):
        return self.favArtist

    def getFavTwit(self):
        return self.favTwit

    def getLocation(self):
        return self.location
        

    def welcome(self, name):
        print('Well then, welcome ' + name)
        self.menuChoice()

    def weather(self, location):
        weatherURL = 'http://xml.weather.yahoo.com/forecastrss?p='+location
        weatherXMLStart = 'http://xml.weather.yahoo.com/ns/rss/1.0'
        currentWeather = {}
        dom = minidom.parse(urlopen(weatherURL))
        for currWeather in dom.getElementsByTagNameNS(weatherXMLStart, 'condition'):
            currentWeather['Condition'] = currWeather.getAttribute('text')
            currentWeather['Temp'] = currWeather.getAttribute('temp')
        for loc in dom.getElementsByTagNameNS(weatherXMLStart, 'location'):
            currentWeather['City'] = loc.getAttribute('city')
            currentWeather['State'] = loc.getAttribute('region')
        print('Right Now in ' + currentWeather['City']+  ", " + currentWeather['State'] +" it's " + currentWeather['Condition'] + ' and ' + currentWeather['Temp'] + ' degrees')
        self.secondary()

    def getTweets(self, twit):
        tweetList = []
        twitterURL = 'http://search.twitter.com/search.atom?q=+from:'+twit
        zipLookupStart = 'http://base.google.com/ns/1.0"'
        dom = minidom.parse(urlopen(twitterURL))
        tweetGet = dom.getElementsByTagName("title")
        for tweet in tweetGet:
            tweetList.append(tweet.childNodes[0].nodeValue)
        if tweetList == [' from:'+twit+' - Twitter Search']:
            return ['Sorry, this person is not on twitter']
        else:
            return tweetList

    def getDirections(self, fromPlace, toPlace):
        directionList = []
        directionsURL = 'http://maps.googleapis.com/maps/api/directions/xml?origin='+fromPlace+'&destination='+toPlace+'&sensor=false'
        zipLookupStart = 'http://base.google.com/ns/1.0"'
        dom = minidom.parse(urlopen(directionsURL))
        directionsGet = dom.getElementsByTagName("html_instructions")
        for direction in directionsGet:
            directionList.append(direction.childNodes[0].nodeValue)
        return directionList

    def getConcerts(self, location):
        concertURL='http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20upcoming.events%20where%20tags%3D%22concert%22%20and%20venue_zip%3D%22'+location+'%22'
        weatherXMLStart='http://www.yahooapis.com/v1/base.rng'
        concertList={}
        dom = minidom.parse(urlopen(concertURL))
        for event in dom.getElementsByTagName('event'):
            concertList['Concert'] = event.getAttribute('name')
            concertList['startDate'] = event.getAttribute('start_date')
            concertList['endDate'] = event.getAttribute('end_date')
            concertList['startTime'] = event.getAttribute('start_time')
            concertList['endTime'] = event.getAttribute('end_time')
            concertList['streetAddress'] = event.getAttribute('venue_address')
            concertList['City'] = event.getAttribute('venue_city')
            concertList['State']=event.getAttribute('venue_state_code')
            concertList['Venue'] = event.getAttribute('venue_name')
        
    
        if concertList== {}:
            print('Sorry, there are no concerts in your area.')
            self.convo()
        else:
            print('Nearest Concert')
            print('Concert:', concertList['Concert'])
            print('Start Date:', concertList['startDate'])
            print('End Date:', concertList['endDate'])
            print('Starts at ', concertList['startTime'])
            print('Ends at ', concertList['endTime'])
            print('Is at', concertList['Venue'])
            print('Which is located at', concertList['streetAddress'] +', '+ concertList['City']+ ', ' +concertList['state'])
            self.secondary()


    def menuChoice(self):
        mode = input('Do you want to have a conversation, or do you just want something quick? ')
        modeList = mode.split()
        if 'conversation' in modeList:
            self.conversation()
        elif 'quick' or menu in modeList:
            self.menu('Null')
        else:
            print("I'm sorry, I didn't get that")
            self.menuChoice()
            
        

    def conversation(self):
        print("Great! Let's talk!")
        option = input('What do you want to do? ')
        self.selector(option)
        
    def convo(self):
        option = input('What do you want to do? ')
        self.selector(option)

    def secondary(self):
        again = input('Anything else you want some help with? ')
        again = again.lower()
        if again == 'yes':
            self.convo()
        else:
            print('See you soon!')
            return
    
    def menu(self, errorText):
        learning = open('myLifeLearning', 'a')
        print('Please select a number correspoonding to your attempted query')
        print(1, 'Weather')
        print(2, 'Twitter')
        print(3, 'Directions')
        print(4, 'Concerts')
        selectedItem = int(input('What is your selection? '))
        if selectedItem == 1:
            for item in errorText:
                learning.write(item + '#$@' + 'weather'+ ' ' + '\n')
            learning.close()
            location = input('Where do you want to find the weather? (zip code only) ')
            if re.match('^\d{5}(-\d{4})?$', str(location)) != None:
                self.weather(location)
            else:
                self.menu(errorText)
        elif selectedItem == 2:
            for item in errorText:
                learning.write(item + '#$@' + 'tweet'+ ' ' + '\n')
            learning.close()
            twit = input("Sorry, but who's twitter handle did you want agian? ")
            print('Great, thanks!')
            self.getTweets(twit)
        elif selectedItem == 3:
            for item in errorText:
                learning.write(item + '#$@' + 'directions'+ ' ' + '\n')
            learning.close()
            fromSource = input("Sorry, but where did you want to start again? ")
            toSource = input("And where did you want to go to? ")
            print('Great, thanks!')
            self.getDirections(fromSource,toSource)
        elif selectedItem == 4:
            for item in errorText:
                learning.write(item + '#$@' + 'concert'+ ' ' + '\n')
            learning.close()
            where = input('Sorry, where is the concert you want to go to again? (zip code only) ')
            if re.match('^\d{5}(-\d{4})?$', str(location)) != None:
                self.getConcerts(where)
            else:
                self.menu(errorText)
    def selector(self, option):
        optionList = []
        load = '///// LOADING '
        load2 = ' ///////'
        error = "I'm sorry, I didn't get that"
        option = option.lower()
        optionList = option.split()
        learning = open('myLifeLearning', 'r')
        if 'weather' in optionList:
            if 'in' in optionList:
                loc = optionList.index('in') + 1
                city = optionList[loc]
                state = optionList[loc+1]
                zipLookupURL = 'http://where.yahooapis.com/geocode?q='+city+state+'&appid=[NrabNx7e]'
                zipLookupStart = 'ResultSet version="1.0"'
                dom = minidom.parse(urlopen(zipLookupURL))
                zipGet = dom.getElementsByTagName("uzip")[0]
                zipcode = zipGet.childNodes[0].nodeValue
                self.weather(zipcode)
            else:
                if 'current' in optionList:
                    self.weather(self.getLocation())
                else:
                    print(error)
                    self.menu(option)

        elif 'tweets' in optionList:
            print(load+'TWEETS'+load2)
            if 'favorite' in optionList:
                tweets = self.getTweets(self.getFavTwit())
            else:
                twitFrom = optionList.index('from')
                twit = optionList[twitFrom+1]
                tweets = self.getTweets(twit)
            for tweet in tweets:
                print(tweet)
                print('---')
                print('')
            self.secondary()
            

        elif 'directions' in optionList:
            if 'from' in optionList:
                if 'to' in optionList:
                    i = 0
                    print(load+'DIRECTIONS'+load2)
                    direction = optionList.index('from')
                    to = optionList.index('to')
                    directionFrom = optionList[direction+1]
                    directionTo = optionList[to+1]
                    directions = self.getDirections(directionFrom, directionTo)
                for nav in directions:
                    i = i+1
                    navNoHTML = re.compile(r'<.*?>')
                    print(i, navNoHTML.sub('', nav))
            else:
                print('Please specify where you want to go, and where you are coming from')
            self.secondary()
                

        elif 'concerts' in optionList:
            loc = optionList.index('near') + 1
            city = optionList[loc]
            state = optionList[loc+1]
            zipLookupURL = 'http://where.yahooapis.com/geocode?q='+city+state+'&appid=[NrabNx7e]'
            zipLookupStart = 'ResultSet version="1.0"'
            dom = minidom.parse(urlopen(zipLookupURL))
            zipGet = dom.getElementsByTagName("uzip")[0]
            zipcode = zipGet.childNodes[0].nodeValue
            self.getConcerts(zipcode)

                
        elif option == 'no':
            print('Goodbye')
            return

        else:
            learningDict = {}
            for line in learning:
                learningList = []
                learningList = line.split('#$@')
                learningDict[learningList[0]] = learningList[1]
            
            validate = learningDict.get(option, None)

            correctText = self.eliminator(option)
            print(self.eliminator(option))
            if validate!=None:
                else:
                    if 
                mentList = learningList[1].split()
                if mentList[0] == 'weather':
                    loc = input('Sorry, but what zip code did you want again? ')
                    if re.match('^\d{5}(-\d{4})?$', loc)!=None:
                        self.weather(loc)
                elif mentList[0]=='twit':
                    twit = input('Sorry, which twitter handle did you want? ')
                    tweets = self.getTweets(twit)
                    print(tweets)
                elif mentList[0]=='directions':
                    fromPlace = input('Sorry, where were you starting from again? ')
                    toPlace = input('Sorry, where were you going to again? ')
                    self.getDirections(fromPlace,toPlace)
            else:
                print(error + '. Switching to Menu Mode')
                self.menu(correctText)
        option = ""

    def eliminator(self, errorText):
        errorList = []
        correctList = re.split("what|where|when|I|me|you|now|currently|about|the|a|now|yet", errorText)
        for item in correctList:
            if re.match('[a-zA-Z0-9]*', item) != None:
                errorList.append(item)
                
        return errorList
   
