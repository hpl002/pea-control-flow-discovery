# readme
Service built using the [PM4PY](https://github.com/pm4py) library.  

Simple service for discovering a process model from a .XES log  
Simply pass in a valid .XES log and get pack the discovered process model in the form of a valid petri net.  
All generated models are validated before being passed back to the client.

## Methods
Supports all methods that the PM4PY library provides. These are:  
   1. Alpha miner      
   2. Inductive miner
      1. inductive miner
      2. inductive miner infrequent
      3. inductive miner directly-follows       
   3. Heuristic miner     


## Validation
The resulting model is checked for syntactic validity and measured according to the four quality dimensions.
1. fitness
2. simplicity
3. precision
4. generalization       