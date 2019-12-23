# Circular Belief Propagation Simulation
[Belief propagation](https://en.wikipedia.org/wiki/Belief_propagation) is a model for explaining sensory perception. It can be represented as a hierarchical neural network or a node graph with nodes of causal factors. The highest node being the prior expectactions and the lowest nodes being the sensory information. The messages exchanged between the nodes are combined with certain confidence levels, or beliefs, in order to account for sensory observations. 

 ![alt text](https://github.com/SuhritD/PCBS-project/blob/master/Ayy%20lmao.png "Node Graph")
 
 Two nodes i and j, where i is above j in the graph will communicate the messages based on the previous belief. 
 
 ![alt text](https://github.com/SuhritD/PCBS-project/blob/master/Capture.PNG)
 
 where the weight is a function of the probability of making an observation based on the higher node's input - 
 ![alt text](https://github.com/SuhritD/PCBS-project/blob/master/W.PNG) 
 
 The belief of a node is the sum of all incoming messages - 
 ![alt text](https://github.com/SuhritD/PCBS-project/blob/master/b.PNG)
 
 The message in the reverse direction is subtract in this case with a factor α, that can be seen as an inhibitory connection to prevent the message from being recurrent. 
 
 In the case of an imbalance in exhitatory and inhibitory connections in the brain, the confidence in a certain observation can be overestimated from little information. The belief from a top down node could be reverberated as a bottom up information to boost confidence about seeing something - a circular inference. Schizophrenics show positive symptoms like hallucinations and delusions that studies have shown could be explained by [circular belief propagation](https://academic.oup.com/schizophreniabulletin/article/42/5/1124/2414016).
 
 
 I will create a simple model of a node graph with 6 nodes as shown in the figure above. I will compare the computed beliefs of sensory evidences based on whether or not the top down or bottom up connections are disrupted. All equations about belief propagation applied can be found [here]. 
 ![alt text]
 
 # Simulations 
 ## 
 

[here]: https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/brain/136/11/10.1093_brain_awt257/3/awt257_Supplementary_Data.zip?Expires=1578341001&Signature=y6luI7Pil3mD-OqDYChLIsVoNk4ev2r1sMzwQessujtYe2gs0AGiBhiIF~Y0zUdh7GYVKN1KrUGg7SdaFuQj3Tix46ZIqsDXCGrfNc~AP5Of3M8kcNULcwHSPt5eDcVe9z7AI8HoIflqg6dEyG3dNOvK658O1HsUx-zUmt0ZR~ltqJuhK1eGOfJhzqv-agYcZFmt4Mt8ECe8rwxGBiwrC-kz6LpYJ3NzaejK1H5mo9e-fqmEmWMIVdnmuphqFvU~ey-59TAuzAjUyX3ayXHbooo8WhEpvoc2zWUYf9Dri5J296xG6T~hGXz2JdDYfHvFC-3dGiTM5mn7pmzdDhhFfA__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA
