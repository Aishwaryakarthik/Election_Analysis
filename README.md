Election_Analysis

Project Overview

A Colorado Board of Elections employee assigned the following tasks to complete the election audit of a recent local congressional election.

1.	Calculate the total number of votes cast.
2.	Get a complete list of candidates who received votes.
3.	Calculate the total number of votes for each candidate received.
4.	Calculate the percentage of votes each candidate won.
5.	Determine the winner of the election based on popular vote.
6.	Calculate the voter turnout for each county.
7.	Calculate the percentage of votes from each county out of the total.
8.	Determine the county with the highest turnout.

Resources

1.Data Source: election_results.csv

2.Software: Python 3.7.6, Visual Studio Code Editor.

Summary

The analysis of the election shows that:

	There were 369,711 votes cast in the election.

The candidates were:

1.Charles Casper Stockham.

2.Diana DeGette.

3.Raymon Anthony Doane.

The candidate results were:

1.Charles Casper Stockham received 23.0% of the vote, for a total of 85,213 votes.

2.Diana DeGette received 73.8% of the vote, for a total of 272,892 votes.

3.Raymon Anthony Doane received 3.1% of the vote, for a total of 11,606 votes.

The winner of the election was:

  Diana DeGette, who received 73.8% of the vote for a total of 272,892 votes.

The voter turnout for each county was:

1.Jefferson produced 10.5% of voters, for a total of 38,855 voters.

2.Denver produced 82.8% of voters, for a total of 306,055 voters.

3.Arapahoe produced 6.7% of voters, for a total of 24,801 voters.

The county with the largest voter turnout was:

	Denver, which produced 82.8% of voters, for a total of 306,055 voters.

This result can also be seen in the text file:
<img width="418" alt="pypoll_challenge_textfile_results" src="https://user-images.githubusercontent.com/99555513/158088613-40ff99d0-431f-40e8-ac53-7aa46cbfa2ad.png">


Election-Audit Summary

Expanding the Election Audit to include voter turnout by county with candidates results has been a great way to take advantage of the convenience a script provides. 

The added insight can be a guide for future election performance, so that you may properly allocate resources where turnout is low or demographics are hard to reach.
A little time invested into customizing the script can provide on-demand analysis for years to come.
Modifying the script to produce turnout results by county is just one of many ways that minor adjustments to the code can reveal critical data. 

For example, we could also dive deeper and determine what percentage of each county voted for each candidate by adding an if-statement to the code. 
These type of Decision Statements helps the code to run calculations and all we've done is provide it with a data file.

Similarly, if this were a federal election, we could use the same script and change the county to states.
In short, no matter the number of candidates or counties, the script used to perform the Election Audit can be a valuable resource for the board.






