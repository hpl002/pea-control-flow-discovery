import pm4py
log = pm4py.read_xes('running-example.xes')
net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(log)
pm4py.view_petri_net(net, initial_marking, final_marking, format="svg")
