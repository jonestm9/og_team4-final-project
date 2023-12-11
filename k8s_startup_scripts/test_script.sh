#!/bin/bash

INGRESS_CONTROLLER="172.31.71.218"
LOAD_BALANCER="172.31.71.218"
INGRESS_PORT="8080"

# Define the demo domains
DEMO1="demo1.localdev.me"
DEMO2="demo2.localdev.me"

# Number of requests to make
NUM_REQUESTS=100

# Function to make requests and collect latency data
function make_lb_request {    
    # Record start time
    start_time=$(date +%s%N)
    
    # Make the request
    curl -sI -H "Host: $1" http://172.31.71.218 > /dev/null
    
    # Record end time
    end_time=$(date +%s%N)
    
    # Calculate latency in milliseconds
    latency=$(( ($end_time - $start_time) / 1000000 ))
    
    # Return latency for further processing
    echo "$latency"
}

function make_ingr_request {
    # Record start time
    start_time=$(date +%s%N)
    
    # Make the request
    curl -sI http://$1:8080/ > /dev/null
    
    # Record end time
    end_time=$(date +%s%N)
    
    # Calculate latency in milliseconds
    latency=$(( ($end_time - $start_time) / 1000000 ))
    
    # Return latency for further processing
    echo "$latency"
}

# Array to store latency data
declare -a ingress_latencies_1
declare -a ingress_latencies_2
declare -a load_balancer_latencies_1
declare -a load_balancer_latencies_2

# Loop to make requests to Ingress controller
for ((i=1; i<=NUM_REQUESTS; i++)); do
    ingress_latencies_1+=("$(make_ingr_request "$DEMO1")")
    ingress_latencies_2+=("$(make_ingr_request "$DEMO2")")
done

# Loop to make requests to Load Balancer
for ((i=1; i<=NUM_REQUESTS; i++)); do
    load_balancer_latencies_1+=("$(make_lb_request "$DEMO1")")
    load_balancer_latencies_2+=("$(make_lb_request "$DEMO2")")
done

# Function to calculate average latency
function calculate_average_latency {
    local latencies=("${@}")
    local total=0
    
    for latency in "${latencies[@]}"; do
        total=$((total + latency))
    done
    
    local average=$((total / ${#latencies[@]}))
    echo "Average Latency: $average ms"
}

# Calculate and print average latency for Ingress controller requests
echo "Ingress Controller Latencies (Host 1):"
calculate_average_latency "${ingress_latencies_1[@]}"

# Calculate and print average latency for Load Balancer requests
echo "Load Balancer Latencies (Host 1):"
calculate_average_latency "${load_balancer_latencies_1[@]}"

echo "Ingress Controller Latencies (Host 2):"
calculate_average_latency "${ingress_latencies_2[@]}"

# Calculate and print average latency for Load Balancer requests
echo "Load Balancer Latencies (Host 2):"
calculate_average_latency "${load_balancer_latencies_2[@]}"

