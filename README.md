# Circular Belief Propagation Simulation
[Belief propagation](https://en.wikipedia.org/wiki/Belief_propagation) is a model for explaining sensory perception. It can be represented as a hierarchical neural network or a node graph with nodes of causal factors. The highest node being the prior expectactions and the lowest nodes being the sensory information. The messages exchanged between the nodes are combined with certain confidence levels, or beliefs, in order to account for sensory observations. 

 ![alt text](https://github.com/SuhritD/PCBS-project/blob/master/Ayy%20lmao.png "Node Graph")
 
 Two nodes i and j represent certain causes, where i is above j in the graph will communicate the messages based on the previous belief. An example could be of nodes 5 and 6 being green and brown perception and node 1 being the presence of a tree, with leaves and branches. 
 
 ![alt text](https://github.com/SuhritD/PCBS-project/blob/master/Capture.PNG)
 
The message in the reverse direction is subtraced with a factor α, that can be seen as an inhibitory connection to prevent the message from being recurrent. The weight is a function of the probability of making an observation based on the higher node's input - 
 ![alt text](https://github.com/SuhritD/PCBS-project/blob/master/W.PNG) 
 
 The belief of a node is the sum of all incoming messages - 
 ![alt text](https://github.com/SuhritD/PCBS-project/blob/master/b.PNG)
 
 In the case of an imbalance in exhitatory and inhibitory connections in the brain, the confidence in a certain observation can be overestimated from little information. The belief from a top down node could be reverberated as a bottom up information to boost confidence about seeing something - a circular inference. Schizophrenics show positive symptoms like hallucinations and delusions that studies have shown could be explained by [circular belief propagation](https://academic.oup.com/schizophreniabulletin/article/42/5/1124/2414016).
 
 
 I will create a simple model of a node graph with 6 nodes as shown in the figure above and compare the computed beliefs of sensory evidences based on whether or not the top down or bottom up connections are disrupted. All equations about belief propagation applied can be found [here]. 

 
 # Simulations 
 Let us consider the conditional probabilities of the nodes being linked as 0.9 upon presence and 0.1 upon absence (the probability of j being present when i is present is 0.9 and 0.1 when i is absent). The sensory evidence coming to nodes 5 and 6 are constant clamping messages, and an external message to node 1 is used to represent prior beliefs. The beliefs are represented as Log Odds Ratio (LOR), or the log of probability of a cause being present divided by the probability of a cause being absent.     
 ## Normal Belief Propagation 
 During normal inference, the ascending and descending inhibitory connections are complete (α=1), whereas circular inference has impaired connections (α=0.1). If there is only sensory information, the external message of nodes 5 and 6 are set.
 ```python
 extMessage={1:0,5:0,6:0}
 asc=desc=1
 ...
 extMessage[1]=0
 extMessage[5]=extMessage[6]=2  
 ```
In case of strong sensory information (The LOR of the sensory causes are twice as like to be seen than not seen), then the probabilities of the beliefs are high. We can plot the belief probabilities over 20 iterations of belief propagation to compare the causes over impaired and normal loops. 
```python
def prob(x):
    return (1/(1+np.exp(-x)))
...
LOR=np.zeros((20,6))
for iter in range(20):
    update(Belief)
    LOR[iter]=Belief[1:7]
for cause in range(6):
 plt.ylim(0,1)
 plt.xticks([0,5,10,15,20])
 plt.xlabel('Iterations')
 plt.ylabel('Probability of Belief')
 plt.plot(prob(LOR.T[cause]))
 ```
 
 ![alt text](https://github.com/SuhritD/PCBS-project/blob/master/Sens2.png)
 
 This shows that the causes are slightly higher for impaired loops, but still quite similar to normal belief propagation. We can repeat the simulation for only high negative prior information, where the confidence should be low for perception of a cause (as the stimulus is twice as likely to be absent than being present).
 
```python
extMessage[1]=-2
extMessage[5]=extMessage[6]=0
```
In this case, the impaired beliefs are similar to normal belief propagation but slightly lower. 

![alt text](https://github.com/SuhritD/PCBS-project/blob/master/Prior%20High.png)

However, if the sensory information is weak (when an ambiguous stimulus is perceived), we can see the differences between impaired and normal connections. 

```python
extMessage[1]=0
extMessage[5]=extMessage[6]=0.5
```

![alt text](https://github.com/SuhritD/PCBS-project/blob/master/Senslow.png) 

This shows that impaired loops cause overconfidence of perceiving a stimulus from little sensory information. This could be how hallucinations appear in schizophrenic patients through circular inference. 

Finally, we can check what happens in the case of contradictory sensory and prior information - 

```python
extMessage[1]=-2
extMessage[5]=extMessage[6]=1
```

![alt text](https://github.com/SuhritD/PCBS-project/blob/master/Contra%20norm.png) 

The result is that the beliefs are close to half normally, but reverberting several times in the case of impaired loops. This is a representation of how bizzare beliefs or delusions appear in schizophrenics, as there is no fixed state of perception.  
[here]: https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/brain/136/11/10.1093_brain_awt257/3/awt257_Supplementary_Data.zip?Expires=1578341001&Signature=y6luI7Pil3mD-OqDYChLIsVoNk4ev2r1sMzwQessujtYe2gs0AGiBhiIF~Y0zUdh7GYVKN1KrUGg7SdaFuQj3Tix46ZIqsDXCGrfNc~AP5Of3M8kcNULcwHSPt5eDcVe9z7AI8HoIflqg6dEyG3dNOvK658O1HsUx-zUmt0ZR~ltqJuhK1eGOfJhzqv-agYcZFmt4Mt8ECe8rwxGBiwrC-kz6LpYJ3NzaejK1H5mo9e-fqmEmWMIVdnmuphqFvU~ey-59TAuzAjUyX3ayXHbooo8WhEpvoc2zWUYf9Dri5J296xG6T~hGXz2JdDYfHvFC-3dGiTM5mn7pmzdDhhFfA__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA
