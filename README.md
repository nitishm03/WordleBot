# WordleBot

Backend

In this project, we are aiming to implement a program that can solve wordle. It will be based on the feedback returned from a guessing function and a validation function, which will not contain any more information other than exactly what is given a human player in the original game. While the guessing mechanism will be built to optimize processes and work significantly faster than a human being, the validation mechanism will only be able to provide ‘green’, ‘yellow’, or ‘gray’ at each index of a guess - nothing more.

Frontend

Once the program is functional from a command line, we will attempt to convert it into an interactive web app which allows a user to interact with the bot, potentially alter parameters, and watch the bot generate guesses as it works towards the solution. We plan on employing [whatever tf kinda technologies and libraries one uses in web dev lmao] to create the application.

Performance Targets

Average Number of Guesses: < 4 otherwise you’re better off playing yourself
Runtime: Before the user loses interest watching the program run
Memory: Nowhere close to killing 8GB RAM 

Initial Program Ideas

Limited to 6 guesses, each guess will consist of the following:
  I. Bot “guesses” a word
      A. Pick best possible guess - but what does this actually mean??
        1. General strategy #1: Narrow down list
          a) We can prune anything that doesn’t match our feedback
          b) From the remaining list of words, we guess again using:
              (1) Random guess
              (2) Arbitrary (first, middle, last, etc)
              (3) Probablistic
          c) The problem is, if you get “atch” then you would have been better off guessing incorrect words deliberately to avoid common prefix
        2. Which brings us to general strategy #2 - start with an initial of 
      B. Pass through validator and store feedback array
        1. If the word is the answer, return success
        2. Otherwise:
          a) Eliminate answers that do not match with all feedback stored so far
