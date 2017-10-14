# Epidemic Spread through Trade Routes in Medieval Europe and Asia

## Lucy Wilcox and Kaitlyn Keil

**Abstract** 
In Gomez and Verdu’s paper *Network theory may explain the vulnerability of medieval human settlements to the Black Death pandemic*. They model infection patterns in Europe and Asia due to the plague and find that hub cities are reinfected more frequently. We extended this work by adding a quarantine response to examine how the spread of the diseases is impacted by varying responses. We also examine the result of quarantining only hub cities. To do this we removed nodes from our network according to various quarantine rates. We find that quarantining hub cities prevents a larger number of cities from being infected on a per city quarantined basis when the transmission rate is low but has less of an overall impact due to the small number of hubs.

_____________________________________________________________

Gomez and Verdu use historical trade and pilgrimage route data to create a network between cities in Europe and Asia during the plague. They start the plague in different Asian cities and let it run through their network with varying transmission rates. Our model uses these same data to create a network, with which we simulate the spread of infection. 

We find that the nodes in our model have a similar degree distribution to the original model. In the figures below our degree boxplot is displayed on the left and Gomez and Verdu's is on the right: 

<img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/initial_degree_boxplot.png" width="400"> <img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/theirdegree2.png" width="400">

However, some elements of our model did not match Gomez and Verdu's. Despite using the same data sets and following the code that they publish. For example, the number of cities in our graph is 1300 compared to their 1311 cities. We also do not have ids for many of the possible starting cities that Gomez and Verdu name. Our closeness coefficient distribution is about three degrees of magnitude higher than theirs but otherwise very similar. We are not sure if this is due to differences between the functions that we each use to calculate closeness or if it is due to a difference in our model.

We look into what might happen if cities had been able to immediately and completely quarantine themselves when the plague began to spread. From this, we calculate the effectiveness of different responses to contain the plague for different transmission rates; first, if any city could potentially quarantine itself, and then if only hub cities (cities with a higher degree - which we defined as being a degree of 7 or above) respond. We chose hub cities to be defined as 7 degrees or above somewhat arbitrary and suggest different values be tested. This type of modeling can be extrapolated to the spread of disease in a smaller field, or suggest ways to react to sickness in a community. We also hope to identify the maximum number of cities that can be saved per quarantined city based on which and how many cities are quarantined.

To do this, we iterate through a set quarantine rates: 0, 0.05, 0.1, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95. For each transmission and quarantine rate, we removed a percentage of the cities (nodes) before the simulation runs, according to the quarantine rate. Once these cities are removed, we begin the infection in a single city in central Asia, as listed by the original supplementary material. For every edge connecting this city to another, the percent chance the infection will spread is equal to the transmission rate. Every time step allows each city to attempt to infect each of its neighbors once. Cities are allowed to be reinfected, which increases the overall infection count of the simulation. We also keep track of the number of cities infected, regardless of the number of times they have been re-infected. We run this simulation for 100 time steps. For each quarantine and transmission rate, we run the simulation 100 times before taking the average number of total infections and number of infected cities for each set of rates. For removing hubs, we repeat this process, but only cities with more than 6 edges are considered for removal.

We find that as the quarantine rate goes up, the number of infections and cities infected decreases at an almost linear rate between quarantine rates of 0 and 0.5, then flattens with few infected cities regardless of the transmission rate:

<img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/plot_all2.png" width="500">

The decrease in the number of cities infected and the number of infections follows the same pattern when all cities are able to be quarantined. However, the slope in the total number of infections is different for each transmission rate. We will be focusing mainly on the number of cities infected as a representation of how badly the disease has spread.

If only hubs are considered for quarantine the number of infection and the number of cities infected also decreases more quickly as the quarantine response rate increases. This behavior is more evident at higher transmission rates:

<img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/plot_hub2.png" width="500">

The number of cities infected is similar for each quarantine rate when the transmission rate is 0.5 and 0.75. However, when the transmission rate is 0.15, fewer cities are infected at each quarantine rate. This data can be seen in detail in Table 1 and Table 2.

When we compare the number of cities infected for any city removed to the number of cities infected when only hubs are removed, we find that the number of cities infected with only hubs being quarantined is much larger. We believe that this is due to the fact that there are only 80 cities which meet our criteria of hub cities compared to the total 1300 cities, this means that when the quarantine rate is 0.25% there are 325 cities being quarantined in the non-hub only model compared to 20 cities in the hub only model. 

To answer our question of what the maximum number of cities saved per city quarantined is, we determine that when the transmission rate is 0.15% quarantining 76 (0.95%) of the hubs causes the number of cities infected to drops to around 160. To achieve similar results when quarantining any city about 300 cities would need to be quarantined. We display this by graphing the ratio of non-infected cities in the graph to cities under quarantine (removed from the graph) for our model where any city can be quarantined and where only hub cities can be quarantined.

<img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/safe_per_quarantine_all.png" width="400"> <img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/safe_per_quarantine_hub.png" width="400">

This shows us that when the transmission rate is low, at 0.15, it is more effective to quarantine hubs. Each hub quarantined saves between 6 and 14 other cities compared to between 2.5 and near 0 when any city can be quarantined. At higher transmission rates the number of cities saved per quarantined hub is below 2, this is similar to when any city is quarantined. 

As more hubs are quarantined, the number of cities saved per quarantine is higher. This is different than when any city is quarantined, in which case as more cities are quarantined, the number of cities saved per quarantine decreases. This is partly because the number of cities infected flatlines at around a quarantine rate of 0.5 and at this point the number of saved cities per quarantined city drops as the number of cities quarantined increases. However, the number of cities saved per quarantined city decreases at low transition rates and is relatively flat at higher rates before a quarantine rate of 0.5 is reached. Future work could involve testing the model with a lower definition of what a hub is to see if there is a point where the number of cities saved per city quarantined is mostly constant regardless of the quarantine rate. 

From our results, we see that if 50% of all cities are under quarantine, less than 10% of the remaining cities will become infected. In effect, this has shut down the spread of disease, no matter what the transmission rate. This low number might be because, at this rate of quarantine, the starting city has a 50% chance of quarantining itself, preventing the spread of the disease. A similar result of shutting down the spread of disease can be achieved by quarantining almost all hub cities at low transmissions rates but is not effective at higher transmission rates.

If our model accurately reflects the spread of disease, we would suggest focusing on quarantining hubs at lower transmission rates and quarantining as many cities as possible, up to 50%, at higher rates.

A more refined model might remove cities as the simulation progresses, depending on the number of infected neighboring cities as well as the quarantine rate. The model also could include an inverse relationship between transitivity and distance, as the disease is less likely to pass from distant cities.

## Appendix

| Transmission Rate | 0.15            | 0.5             | 0.75           |
|-------------------|-----------------|-----------------|----------------|
| Quarantine Rate   | Cities Infected | Cities Infected | Cities Infected|
| 0                 | 1272.95         | 1295.97         | 1296           |
| 0.05              | 1084.48         | 1175.58         | 1149.57        |
| 0.15              | 713.99          | 845.01          | 826.23         |
| 0.25              | 348.31          | 562.74          | 556.17         |
| 0.35              | 93.2            | 195.86          | 210.14         |
| 0.45              | 31.17           | 42.26           | 58.44          |
| 0.55              | 6.14            | 6.05            | 9.89           |
| 0.65              | 3.04            | 2.15            | 3.08           |
| 0.75              | 1.7             | 1.68            | 1.53           |
| 0.85              | 1.14            | 1.09            | 1.05           |
| 0.95              | 1               | 1               | 1              |

**Table 1**: This table shows the average number of cities infected per each quarantine and transmission rate where any city can be quarantined.
_________________________________________________________________________________________

| Transmission Rate | 0.15            | 0.5             | 0.75            |
|-------------------|-----------------|-----------------|-----------------|
| Quarantine Rate   | Cities Infected | Cities Infected | Cities Infected |
| 0                 | 1266.46         | 1296            | 1296            |
| 0.05              | 1253.68         | 1290.05         | 1290.08         |
| 0.15              | 1213.54         | 1277.23         | 1277.46         |
| 0.25              | 1111.31         | 1261.11         | 1262.46         |
| 0.35              | 1061.05         | 1243.86         | 1243.71         |
| 0.45              | 957.69          | 1224.24         | 1220.59         |
| 0.55              | 817.31          | 1194.76         | 1199.66         |
| 0.65              | 573.79          | 1162.17         | 1167.24         |
| 0.75              | 474.32          | 1115.44         | 1115.26         |
| 0.85              | 265.76          | 1056.59         | 1052.61         |
| 0.95              | 159.55          | 964.76          | 967.07          |

**Table 2**:  This table shows the average number of cities infected per each quarantine and transmission rate where only hubs can be quarantined.

## Bibliography 
[Gómez, J. M. and Verdú, M. Network theory may explain the vulnerability of medieval human settlements to the Black Death pandemic.](https://www.nature.com/articles/srep43467) Sci. Rep. 7, 43467; doi: 10.1038/srep43467 (2017).

*Gomez and Verdu create an explanatory model of the networks between cities involved in the black plague to analyze which factors were correlated with the damaged caused. Particularly they analyzed the centrality and local transitivity in the trade and pilgrimage networks. They propose that there is a relation between the severity of the plague and these factors and suggest researching if this pattern holds in the present day.*   


[Concurrency-Induced Transitions in Epidemic Dynamics on Temporal Networks](https://comdig.unam.mx/2017/09/10/concurrency-induced-transitions-in-epidemic-dynamics-on-temporal-networks/); *Onaga, Tomokatsu; Gleeson, James P.; and Masuda, Naoki; Physical Review Letters (6 Sept 2017) 119, 108301.*

In their article, Onaga, Gleeson, and Masuda examine how epidemics (both in physical and viral information space) spread over dynamic, or temporal, networks. They construct these networks through graphs of certain connectivity which discard their edges after a certain time period before being activated and reconnected. Each node has a certain activity potential to represent an individual's tendency to make connections. Through a simulation that combines this model and continuous-time susceptible-infected-susceptible modeling, they predict the pattern of epidemic spread and show that high nodal concurrency enhances epidemics. This model could be extended to examine the effects of two mutually exclusive epidemics with either similar or different connectivity.
