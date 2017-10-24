# Epidemic Spread through Trade Routes in Medieval Europe and Asia

## Lucy Wilcox and Kaitlyn Keil

**Abstract** 

In Gomez and Verdu’s paper *Network theory may explain the vulnerability of medieval human settlements to the Black Death pandemic*, they model infection patterns in Europe and Asia due to the plague to determine how transitivity and network centrality influence the spread of disease, and find that hub cities, which have high centrality and transitivity, are reinfected more frequently. We extend this work by adding a quarantine response, modeled by removing cities from the graph. We examine the impact of quarantining increasing percentages of the total number of cities and of only hub cities. We find that each quarantined hub city prevents a larger number of other cities from becoming infected, but has less of an overall impact due to the small number of hub cities.
_____________________________________________________________

Gomez and Verdu use historical trade and pilgrimage route data to create a network representing cities and major travel routes in Europe and Asia during the plague. They start the plague in different Asian cities and let it run through their network with varying transmission rates to determine how network centrality and transitivity influence the spread of the disease. Network centrality is the impact nodes have on the network based on their degree and their neighbors’ degrees, and transitivity is the number of triangle forms in the network compared to the number of connected triplets. 

Our model uses these same data as much as possible to create a network, with which we simulate the spread of infection for different transmission rates, where the transmission rate is the chance that infection will spread along a connecting edge each timestep. We begin the infection in a single city in central Asia, as listed in the original supplementary material. Every time step allows each city to attempt to infect each of its neighbors once. Cities are allowed to be reinfected, which increases the overall infection count of the simulation. We keep track of the number of cities infected, regardless of the number of times they have been re-infected as well as the total number of infections. In addition, our model examines the effects of varying quarantine rates. For each quarantine rate, we remove a corresponding percentage of the cities (nodes) before the simulation runs. This models a city completely shutting down any incoming or outgoing trade and pilgrimage. Once these cities are removed, we run the simulation 100 times before taking the average number of total infections and number of infected cities for each set of rates. This is the Any City model. We repeat this process for hub cities, where hub cities are defined as cities with a degree of seven or more, this is the Hub City model. There are only 80 hub cities in the original graph, compared to 1300 total cities. We then compare the effects of these two models to see which--quarantining all cities or just the central ones--has a greater impact on the overall health of the network. We consider health to be a lower number of total cities infected by the end of the simulation.

We find that the nodes in our network do not have an identical degree distribution to the original model. Nodes in Gomez and Verdu’s model have slightly higher degree than in our model as seen in Fig. 1 and 2.

<p align="center">
<img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/initial_degree_boxplot.png" width="380"> <img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/theirdegree3.png" width="420">
 <br><br>
  <caption align="bottom"><b>Fig. 1 (left) and Fig. 2 (right) </b> While similar, Gomez' and Verdu's network has a slightly higher degree.</caption>
</p>

However, some elements of our model did not match Gomez and Verdu's, despite using the same data sets and following the code that they publish. For example, the number of cities in our graph is 1300 compared to their 1311 cities. We also do not have ids for many of the possible starting cities that Gomez and Verdu name. Despite these differences, our model runs in a similar manner.

In Fig. 3 we graph infected cities and total infections in the Any City model to see how the number of infected cities decreases with more quarantined cities.

<p align="center">
<img src="https://github.com/LucyWilcox/Plague/blob/master/reports/total_infections_any.png" width="500">
  <br><br>
  <caption align="bottom"><b>Fig. 3</b></caption>
</p>

Fig. 3 shows that in the Any City model, as the quarantine rate goes up, the number of infections and cities infected decreases at an almost linear rate between quarantine rates of 0 and 0.5, then flattens with few infected cities regardless of the transmission rate. This is because at high quarantine response rates, the initial city infected or those directly around it are likely to be quarantined, preventing any further spread of the disease. The transmission rates, while noticeably different for low quarantine rates, do not have much impact as quarantine rates pass 50%.

The results in Fig. 4 underwent the same process as those shown in Fig. 3 but use data from the Hub City model.

<p align="center">
<img src="https://github.com/LucyWilcox/Plague/blob/master/reports/total_infections_hubs.png" width="500">
  <br><br>
  <caption align="bottom"><b>Fig. 4</b></caption>
</p>

In Fig. 4, we see that while increasing quarantine responses still cause a decrease in the spread of infection in the Hub City model, the general slope of the line is shallower. Even when nearly all hub cities are quarantined, all but the lowest transmission rate infect a large percentage of the total cities, resulting in a generally less healthy network if the only metric is the number of infected cities. This does not mean, however, that quarantining hub cities is ineffectual.

Fig. 5 and 6 show the ratio of uninfected, unquarantined cities to number of cities quarantined. While the Any City model has a greater overall reduction in the number of infected cities, each city removed has lower impact, with a maximum of less than 2.5 cities saved for a single city removed. This is because many of the quarantined cities have few connections, and so would not have spread the disease far regardless. However, in the Hub City model, as many as 15 unquarantined cities remain healthy for every quarantined hub, because the quarantined cities have a higher degree. This means that quarantining only 76 (95%) of the hub cities has the same impact on the overall health of the graph as quarantining approximately 300 random cities for low transmission rates.


<p align="center">
<img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/safe_per_quarantine_all.png" width="400"> <img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/safe_per_quarantine_hub.png" width="400">
  <br><br>
  <caption align="bottom"><b>Fig. 5 (left) and Fig. 6 (right) </b></caption>
</p>

Fig. 5 and 6 demonstrate that at low transmission rates, such as 0.15, it is more effective to quarantine hubs. Each hub quarantined saves 6-14 other cities compared to 1-2.5 in the Any City model. At higher transmission rates, the number of cities saved per quarantined hub is generally below 2, so the two methods have similar impact.

As more hubs are quarantined, the number of cities saved per quarantine is higher for the Hub City model, as seen by the ratio in Figure 6 increasing. This is different than in the Any City model, where the ratio decreases as the quarantine rate goes up due to the low number of cities remaining in the network.

From our results, we see that if 50% of cities in the Any City model are under quarantine, less than 10% of the remaining cities will become infected. In effect, this has shut down the spread of disease, no matter what the transmission rate. This low number might be because, at this rate of quarantine, the starting city has a 50% chance of quarantining itself, preventing the spread of the disease. A similar result of shutting down the spread of disease can be achieved by quarantining almost all hub cities at low transmissions rates but this method is not effective at higher transmission rates.

If our model accurately reflects the spread of disease, we would suggest focusing on quarantining hubs at lower transmission rates and quarantining as many cities as possible, up to 50%, for highly transmissive diseases.

A more refined model might remove cities as the simulation progresses, depending on the number of infected neighboring cities as well as the quarantine rate. The model also could include an inverse relationship between transitivity and distance, as the disease is less likely to pass from distant cities. Future work could include testing the model with a lower definition of what a hub is to see if there is a point where the number of cities saved per city quarantined is mostly constant regardless of the quarantine rate.

To repeat our experiment, fork and clone [this repository](https://github.com/LucyWilcox/Plague/tree/master/code). It contains the .py and datafiles needed to run the simulation. Our simulation can be run with the code found [here](http://localhost:8890/notebooks/epidemic_simulator.ipynb), and the processing of results can be done [here](http://localhost:8890/notebooks/csv_plotting.ipynb).

## Bibliography 
[Gómez, J. M. and Verdú, M. Network theory may explain the vulnerability of medieval human settlements to the Black Death pandemic.](https://www.nature.com/articles/srep43467) Sci. Rep. 7, 43467; doi: 10.1038/srep43467 (2017).

*Gomez and Verdu create an explanatory model of the networks between cities involved in the black plague to analyze which factors were correlated with the damaged caused. Particularly they analyzed the centrality and local transitivity in the trade and pilgrimage networks. They propose that there is a relation between the severity of the plague and these factors and suggest researching if this pattern holds in the present day.*   


[Concurrency-Induced Transitions in Epidemic Dynamics on Temporal Networks](https://comdig.unam.mx/2017/09/10/concurrency-induced-transitions-in-epidemic-dynamics-on-temporal-networks/); Onaga, Tomokatsu; Gleeson, James P.; and Masuda, Naoki; Physical Review Letters (6 Sept 2017) 119, 108301.

*In their article, Onaga, Gleeson, and Masuda examine how epidemics (both in physical and viral information space) spread over dynamic, or temporal, networks. They construct these networks through graphs of certain connectivity which discard their edges after a certain time period before being activated and reconnected. Each node has a certain activity potential to represent an individual's tendency to make connections. Through a simulation that combines this model and continuous-time susceptible-infected-susceptible modeling, they predict the pattern of epidemic spread and show that high nodal concurrency enhances epidemics. This model could be extended to examine the effects of two mutually exclusive epidemics with either similar or different connectivity.*
