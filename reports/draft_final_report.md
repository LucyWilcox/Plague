# Epidemic Spread through Trade Routes in Medieval Europe and Asia

## Lucy Wilcox and Kaitlyn Keil

**Abstract** 
In Gomez and Verdu’s paper *Network theory may explain the vulnerability of medieval human settlements to the Black Death pandemic*. They model infection patterns in Europe and Asia due to the plague and find that hub cities are reinfected more frequently. We extended this work by adding a quarantine response to examine how the spread of the diseases is impacted by varying responses. We also examine the result of quarantining only hub cities. To do this we removed nodes from our network according to a certain rate. We find that quarantining hub cities prevents a larger number of cities from being infected on a per city quarantined basis, but has less of an overall impact due to the small number of hubs.

Gomez and Verdu use historical trade and pilgrimage route data to create a network between cities in Europe and Asia during the plague. They start the plague and different Asian cities and let it run through their network with varying transmission rates. Our model uses these same data to create a network, and we simulate their reinfection pattern. We look into what might have happened if cities had been able to immediately and completely quarantine themselves when the plague began to spread. From this, we can guess at the minimum percent response to contain the plague for different transmission rates; first if any city could potentially quarantine itself, and then if only hub cities (cities with higher degree - which we defined as being a degree of 7 or above) respond. This type of modeling can be extrapolated to the spread of disease in a smaller field, or suggest ways to react to sickness in a community.

To do this, we iterate through a set quarantine rates which determine what percentage of cities are quarantined and are removed from the graph. For each transmission and quarantine rate, we removed a percentage of the cities (nodes) before the simulation ran, as per the quarantine rate. Once these cities are removed, we begin the infection in a single city in central Asia, as listed by the original supplementary material. For every edge connecting this city to another, there is a percent chance of infection spread equal to the transmission rate. Every time step allows each city to attempt to infect each of its neighbors once. Cities are allowed to be reinfected, which increases the overall infection count of the simulation. We also keep track of the number of cities infected, regardless of the number of times they have been re-infected. We run this simulation for 100 time steps. For each quarantine and transmission rate, we run the simulation 100 times before taking the average number of total infections and number of infected cities for each set of rates. For removing hubs, we repeat this process, but only cities with more than 6 edges are considered for removal.

We find that as the quarantine rate goes up, the number of infections and cities infected decreases at an almost linear rate as seen in Figure 1. If only hubs are considered for quarantine the number of infection and the number of cities infected also decreases at an almost linear rate as seen in Figure 2. 

When we compare the number of cities infected for any city removed to the number of cities infected when only hubs are removed, we find that while the number for low quarantine rates are very similar, as the quarantine rate increases, the number of cities infected with only hubs being quarantined is much larger. This is shown in Figure 3 and Figure 4. We believe that this is due to the fact that there are only 80 cities which meet our criteria of hub cities compared to the total 1300 cities, this means that when the quarantine rate is 0.25% there are 325 cities being quarantined in the non-hub only model compared to 20 cities in the hub only model. 

Though both of these relationships are linear, we find that they have different slopes, this can help us determine the effectiveness of quarantining hubs. The number of cities not infected with per city quarantined is 7.6 on average when only hub cities are quarantined and 2.3 when any city can be quarantined. When the number of cities not infected excludes the quarantined cities the average cities not infected drops to 6.9 when only hub cities are quarantined  and 1.5 when any city can be quarantined. Full data can be found in Table 1 and Table 2. This shows us that if a limited number of cities can be quarantined it is more effective to quarantine hub cities.

Another method we used to more accurately determine the spread of the disease is to compare the number of infected cities to the number of cities in the graph. TODO: INSERT THESE RESULTS.

From these results, we can see that if 50% of the cities are under quarantine, less than 10% of the remaining cities will become infected. In effect, this has shut down the spread of disease, no matter what the transmission rate. This low number might be because, at this rate of quarantine, the starting city has a 50% chance of quarantining itself, preventing the spread of any disease at all.


A more refined model might remove cities as the simulation progresses, depending on the number of infected neighboring cities as well as the quarantine rate. The model also could include an inverse relationship between transitivity and distance, as disease is less likely to pass from distant cities.

## Appendix

<img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/any_city_quarantined_plots.png" width="500">

**Figure 1**: Graphs show the total number of infections and total cities infected for different transmission rates and quarantine response rates. In this set of graphs all cities may be quarantined.

_________________________________________________________________________________________

<img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/quarantined_hubs_plots.png" width="500">

**Figure 2**: Graphs show the total number of infections and total cities infected for different transmission rates and quarantine response rates. In this set of graphs only hub cities may be quarantined.

_________________________________________________________________________________________

<img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/any_heatmap.png" width="500">

**Figure 3**: A heatmap of the total number of cities infected with different transmission and quarantine rates where all cities can be quarantined.

_________________________________________________________________________________________

<img src="https://raw.githubusercontent.com/LucyWilcox/Plague/master/reports/hub_heatmap.png" width="500">

**Figure 4***: A heatmap of the total number of cities infected with different transmission and quarantine rates where only hub cities can be quarantined.

_________________________________________________________________________________________

| Transmission Rate  | Quarantine Rate           | Cities Quarantined  | Cities Infected | Cities Not Infected per Quarantined City | Cities Not Infected in Graph per Quarantined City  |
|--------------------|---------------------------|---------------------|-----------------|------------------------------------------|----------------------------------------------------|
| 0.15               | 0                         | 0                   | 1200            |                                          |                                                    |
| 0.15               | 0.05                      | 65                  | 1100            | 3.08                                     | 2.08                                               |
| 0.15               | 0.1                       | 130                 | 890             | 3.15                                     | 2.15                                               |
| 0.15               | 0.25                      | 325                 | 360             | 2.89                                     | 1.89                                               |
| 0.15               | 0.5                       | 650                 | 21              | 1.97                                     | 0.97                                               |
| 0.25               | 0                         | 0                   | 1300            |                                          |                                                    |
| 0.25               | 0.05                      | 65                  | 1200            | 1.54                                     | 0.54                                               |
| 0.25               | 0.1                       | 130                 | 1000            | 2.31                                     | 1.31                                               |
| 0.25               | 0.25                      | 325                 | 430             | 1.42                                     | 1.68                                               |
| 0.25               | 0.5                       | 650                 | 25              | 1.96                                     | 0.96                                               |
| 0.5                | 0                         | 0                   | 1300            |                                          |                                                    |
| 0.5                | 0.05                      | 65                  | 1100            | 3.08                                     | 2.08                                               |
| 0.5                | 0.1                       | 130                 | 1000            | 2.31                                     | 1.31                                               |
| 0.5                | 0.25                      | 325                 | 480             | 2.52                                     | 1.52                                               |
| 0.5                | 0.5                       | 650                 | 31              | 1.95                                     | 0.95                                               |

**Table 1**: This table shows the number of cities quarantined, cities infected, and the number of cities not infected per city quarantine where any city can be quarantined. We show the number of cities not infected per city quarantined both including and excluding the number of quarantined cities in the total cities not infected.

_________________________________________________________________________________________

| Transmission Rate  | Quarantine Rate           | Cities Quarantined  | Cities Infected | Cities Not Infected per Quarantined City | Cities Not Infected in Graph per Quarantined City  |
|--------------------|---------------------------|---------------------|-----------------|------------------------------------------|----------------------------------------------------|
| 0.15               | 0                         | 0                   | 1300            |                                          |                                                    |
| 0.15               | 0.05                      | 4                   | 1200            | 25                                       | 24                                                 |
| 0.15               | 0.1                       | 8                   | 1200            | 12.5                                     | 11.5                                               |
| 0.15               | 0.25                      | 20                  | 1100            | 10                                       | 9                                                  |
| 0.15               | 0.5                       | 40                  | 820             | 12                                       | 11                                                 |
| 0.25               | 0                         | 0                   | 1300            |                                          |                                                    |
| 0.25               | 0.05                      | 4                   | 1300            | 0                                        | 0                                                  |
| 0.25               | 0.1                       | 8                   | 1300            | 0                                        | 0                                                  |
| 0.25               | 0.25                      | 20                  | 1200            | 5                                        | 4                                                  |
| 0.25               | 0.5                       | 40                  | 1100            | 5                                        | 4                                                  |
| 0.5                | 0                         | 0                   | 1300            |                                          |                                                    |
| 0.5                | 0.05                      | 4                   | 1300            | 0                                        | 0                                                  |
| 0.5                | 0.1                       | 8                   | 1200            | 12.5                                     | 11.5                                               |
| 0.5                | 0.25                      | 20                  | 1200            | 5                                        | 4                                                  |
| 0.5                | 0.5                       | 40                  | 1100            | 5                                        | 4                                                  |

**Table 2**: This table shows the number of cities quarantined, cities infected, and the number of cities not infected per city quarantine where only hub cities can be quarantined. We show the number of cities not infected per city quarantined both including and excluding the number of quarantined cities in the total cities not infected.

## Bibliography 
[Gómez, J. M. and Verdú, M. Network theory may explain the vulnerability of medieval human settlements to the Black Death pandemic.](https://www.nature.com/articles/srep43467) Sci. Rep. 7, 43467; doi: 10.1038/srep43467 (2017).

*Gomez and Verdu create an explanatory model of the networks between cities involved in the black plague to analyze which factors were correlated with the damaged caused. Particularly they analyzed the centrality and local transitivity in the trade and pilgrimage networks. They propose that there is a relation between the severity of the plague and these factors and suggest researching if this pattern holds in the present day.*   


[Concurrency-Induced Transitions in Epidemic Dynamics on Temporal Networks](https://comdig.unam.mx/2017/09/10/concurrency-induced-transitions-in-epidemic-dynamics-on-temporal-networks/); *Onaga, Tomokatsu; Gleeson, James P.; and Masuda, Naoki; **Physical Review Letters** (6 Sept 2017) 119, 108301.*

In their article, Onaga, Gleeson, and Masuda examine how epidemics (both in physical and viral information space) spread over dynamic, or temporal, networks. They construct these networks through graphs of certain connectivity which discard their edges after a certain time period before being activated and reconnected. Each node has a certain activity potential to represent an individual's tendency to make connections. Through a simulation that combines this model and continuous-time susceptible-infected-susceptible modeling, they predict the pattern of epidemic spread and show that high nodal concurrency enhances epidemics. This model could be extended to examine the effects of two mutually exclusive epidemics with either similar or different connectivity.


