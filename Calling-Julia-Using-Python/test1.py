import julia
julia.install()
j=julia.Julia()
x = j.include("test.jl")
print(" ")
print(" ")
print(x)