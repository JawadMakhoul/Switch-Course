def recent_calls(calls, k): # Recent Call Logs
    return calls[-k:] if k > 0 else []

print(recent_calls([1001,1002,1003,1004], 3))
print(recent_calls([1,2], 3))
print(recent_calls([1, 2,3,4,5], 2))
print(recent_calls([],5))