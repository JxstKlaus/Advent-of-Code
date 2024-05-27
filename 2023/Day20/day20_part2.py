#Flip-flop module = %
#default: off
#if high pulse nothing happens
#low pulse switches between on and off
#   turning off sends a low pulse
#   turning on sends a high pulse

#Conjuction module = &
#rememebers the most recent pulse from each input
#default: remembers low pulse
#when a pulse is sent, first it updates its memory
#then if all signals are high it sends a low pulse otherwise sends a high pulse

#broadcaster module
#sends the same pulse that it receives to all destinations

use_real_data = True
if use_real_data: file_name = "day20_input.txt"
else: file_name = "day20_example.txt"

data = [[y[0][0],y[0][1:],y[1].split(", ")] if y[0] != "broadcaster"  else ["",y[0],y[1].split(", ")] for y in [x.strip().split(" -> ") for x in open(f"2023\Day20\{file_name}", "r")]]

modules = {}
for prefix,name,dest in data:
    modules[name] = prefix, dest

#%px --> px: "on"
#&px --> px: {a:0, b:1}
#where 0 and 1 indicates low and high pulses
    
states = {}
for module in modules:
    if modules[module][0] == "%":
        states[module] = "off"
    else:
        states[module] = dict([(name,0)  for name in modules if module in modules[name][1]])

#low pulse:     0
#high pulse:    1

low_pulse_count = 0
high_pulse_count = 0
for _ in range(1000):
    queue = [[0,"button","broadcaster"]]
    while queue != []:
        received_pulse,prev_module_name,module_name = queue[0]
        
        if received_pulse == 1:
            high_pulse_count += 1
        else:
            low_pulse_count += 1

        if module_name in modules:
            pulse = None    
            prefix,destinations = modules[module_name]

            if module_name == "broadcaster":
                pulse = 0

            elif prefix == "%" and received_pulse == 0:
                if states[module_name] == "on":
                    states[module_name] = "off"
                    pulse = 0

                elif states[module_name] == "off":
                    states[module_name] = "on"
                    pulse = 1

            elif prefix == "&":
                states[module_name][prev_module_name] = received_pulse
                all_input_signals = 0
                for input in states[module_name]:
                    all_input_signals += states[module_name][input]
                if all_input_signals == len(states[module_name]):
                    pulse = 0
                else:
                    pulse = 1

            if pulse != None:
                queue += [[pulse,module_name,dest] for dest in destinations]

        queue = queue[1::]

print(f"Day 20 part 1 answer: {low_pulse_count * high_pulse_count}")