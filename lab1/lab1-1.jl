#----TASK1----

summing() = 0.0000001f0 + 100000f0

function mul_sub()
    great = 100000f0
    small = 0.001f0
    for (i) = 1:1000
        great -= small
    end
    return great
end

function mul_sum()
    sum = 0f0
    small = 0.001f0
    big = 100000f0
    for i = 1:1000
        sum += small
    end
    return big - sum
end

print("\nTASK 1\n")
print(summing(), "\n")
print(mul_sub(), "\n")
print(mul_sum(), "\n")

#----TASK2----

function task2(val, length)

    tab = Float32[]
    for i = 1:length
        push!(tab, val)
    end

    sum  = 0f0
    for e in tab
        sum += e
    end
    return sum
end

count_abs_error(val, sum, length) = abs(val - (sum / length))

count_rel_error(val, sum, length) = abs((val - (sum / length)) / val) * 100f0

length = 10000000f0
float_val = 0.561025f0

result = task2(float_val, length)


abs_error = count_abs_error(float_val, result, length)
rel_error = count_rel_error(float_val, result, length)

print("\nTASK 2\n")
print("ABS ERROR: ", abs_error)
print("REL ERROR: ", rel_error, "%\n")
