>A more complex smart contract which allows option(project) leaders to vote for voters.

Based on the simple voting app I bulit before, in which only voters can vote, now I add a new character leader who can also assign points, but to normal voters rather than their corresponding options/projects. The final points of ProjectA-Voter1 is the sum of the points Voter1 assigns for ProjectA and the points LeaderA assigns for Voter1.

For testing, 

1.I use the **Remix online IDE** to compile and deploy the smart contract(connection to the localhost node with **Ganache**).

2.call the function Give_right_to_voters (do either with Remix or with python web3 interaction api)

3.run the flask app, for those authorized voters and leaders, they can vote via browser.



