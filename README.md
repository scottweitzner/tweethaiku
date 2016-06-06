# tweetHaiku
A simple python script that scrapes tweets from a twitter account and randomly generates a haiku.

### How it works
Currently the haikus are based upon the parts of speech patterns for numerous famous haikus. As such some haikus may seem odd due to the terse and symbolic nature of traditional haikus

### To be added
First I would eventually like to integrate this as a twitterbot
Right now the linguistic approach I'm taking is somewhat simple. I would like to implement a finite state machine for pattern matching in order to keep track of both symbols as well as parts of speech. I will actually not be paying attention to syllables as much as I am parts of speech. Traditional haikus actually don't need to follow the 5-7-5 pattern, contrary to popular belief. 

>“I don’t think counting 5,7,5 syllables is necessary or desirable. 
>To reflect the natural world, and the season, is to reflect what is.” 
>—Gary Snyder

Read more here: http://www.nahaiwrimo.com/home/why-no-5-7-5
