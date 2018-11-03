#----TASK2----

using Plots

function kahanSumming(arr::Array{Float32,1})
    sum = 0f0
    err = 0f0

    for i = 1:length(arr)
        y = arr[i] - err
        temp = sum + y
        err = (temp - sum) - y
        sum = temp
    end

    return sum, err
end


array = collect(range(1f0, length=10000000, stop=10000f0))

result, err = kahanSumming(array)

println(result)
println(err)

plot(rand(5,5),linewidth=2,title="My Plot")

png("test")


task5(x0, r, n) = if n == 0
        return x0
    else
        xn = task5(x0, r, n - 1)
        return r * xn*(1 - xn)
    end

matrix = zeros(Float32, 4, 10)

for i = 1:4
    for j = 1:100
        matrix[i,j] = task5(0.6, i, 100+j)
    end
end

matrix

x = [1]
y = [1]

scatter(x,y,title="My Scatter Plot")