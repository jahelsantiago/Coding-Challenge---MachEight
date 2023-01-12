from pair_sums import pair_sums

#write the main function
def main():
    #read the input
    input_text = input("> app ")
    nums, target = input_text.split(" ")
    #cast the input
    nums = [int(n) for  n in nums.split(",")]
    target = int(target)
    #solve the problem
    pair_sums_list = pair_sums(nums, target)
    #print the output
    for pair in pair_sums_list:
        print(f'+ {pair[0]},{pair[1]}')



if __name__ == '__main__':
    main()