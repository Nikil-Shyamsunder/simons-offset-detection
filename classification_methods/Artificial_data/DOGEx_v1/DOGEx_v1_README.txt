This file relates the the Detection of Offsets in GPS timeseries Experiment (DOGEx) 2010. 

Introduction
============
DOGEx is a community experiment launched at EGU 2010 in order to test automated offset detection algorithms against a known truth in the presence of realistic timeseries signal, noise, offset frequency and gaps. It has a similar philosphy to the Southern California Earthquake Center (SCEC) Transient Detection Exercise, but focused on offsets, not detection of anomalous strain transients and has developed independently (and ignorantly) of it.

The experiment is being run jointly by Matt King (Newcastle University, Newcastle upon Tyne, UK; m.a.king@ncl.ac.uk) and Simon Williams (Proudman Oceanographic Laboratory, Liverpool, UK; sdwil@pol.ac.uk). COST Action ES0701 "Improved Constraints on Models of Glacial Isostatic Adjustment" is sponsoring this experiment http://www.cost-es0701.gcparks.com/.

Participation
=============
If you are willing to participate, please email m.a.king@ncl.ac.uk so we can keep you informed of updates or events. The data is available with this readme at the experiment website below.

General Principles
==================
DOGEx is a one-way blind experiment in that the actual offset times and magnitudes are not released with the site timeseries. The data set we supply is a time series of daily NEU coordinates and the formal errors for 50 "sites". These sites are simulated although based on real signal, noise, offset frequency and gaps duration. Users interested in testing offset detection techniques are invited to submit their solutions in the format given below. At regular intervals we will update the community on success rates (EGU, AGU, IGS Workshops etc.). We will work with the authors of the most succesful techniques as and when publication is warranted. The experiment will run until there is no longer need for it.

Important Information
=====================
There is only ONE linear rate per site (despite appearances in some cases). 
There are NO outliers, so outlier editing may lead to erroneous results. 

Experiment Website
==================
http://www.cost-es0701.gcparks.com/working-groups/wg

Timeseries File Format
======================
decimal year   N(m)           E(m)           U(m)          sigmaN(m)      sigmaE(m)      sigmaU(m)
1995.0226    -0.01915857    -0.05686093     0.01769778     0.00840000     0.00610000     0.00890000

decimal years were computed based on the following formula
T = 1970 + (mjd - m70 + 0.5) / 365.25;

Where m70 is 40587 and mjd is Modified Julian Days. 

Submission Format
=================
Please submit to sdwil@pol.ac.uk an ascii text file containing the following information in the EXACT format given: 1) offset times (units: decimal years as above) and magnitudes (units: mm/yr) by site and coordinate component and 2) estimated linear rate (units: mm/yr) by site and component. Complete the header information as shown.

# Contact: First Lastname (Institute, Country; Email)
# Members: First2 Lastname2, First2 Lastname2, ...
# Solution Identifier: 8-char identifier (e.g., NCL_ARM1)
# Technique Information: Brief description of the technique used. Use one line only.
ABXQ OFFSET_N 1999.2233 -2.30 
ABXQ OFFSET_E 1999.2233 10.12
ABXQ OFFSET_U 1999.2233 22.12
ABXQ OFFSET_U 2004.9942 -19.11
ABXQ RATE_N 1.19
ABXQ RATE_E -23.42
ABXQ RATE_U 0.54
AJGJ ...
....
ZOYU RATE_U 10.11

Limitations
===========
We recognise there are limitations in this first experiment. For instance, the sites do not have external data through which many (but not all) offsets are detected in GPS time series, e.g., metadata. On the other hand there are no outliers and only one linear rate, so this makes it easy...

Conditions
==========
Submission of a solution will be taken to mean that the team are willing to participate in the experiment and subsequent publication(s) regardless of the quality of their solution. Only a subset of the submitted solutions may end up in publications and only the teams  responsible for these solutions could appear on author lists.

Date: Feb 24, 2010