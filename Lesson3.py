for total in range(num_experiments):
    result = create_hex_digit(3)

    if result[0:2] == 'BB':
        favourable = favourable + 1

    graphing_data.append(favourable/(total+1))
    theo.append(1/256)
