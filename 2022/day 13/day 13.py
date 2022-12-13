import os


def read_input():
    dir = os.path.dirname(__file__)
    lines = open(dir + '\input.txt', 'r').read().split('\n\n')
    lines = [line.split('\n') for line in lines if line != '']
    return lines


if __name__ == '__main__':
    data = read_input()

    def compare(left, right):
        if type(left) == int and type(right) == int:
            return left < right
        else:
            if type(left) == list and type(right) == list:
                if len(right) > len(left):
                    return False
                elif len(right) < len(left):
                    return True
                else:
                    for i in range(len(left)):
                        compare(left[i], right[i])

            elif type(left) == list and isinstance(right, list) == False:
                compare(left[i], [right[i]])
            elif isinstance(type(left), list) == False and isinstance(right, list) == True:
                compare([left[i]], right[i])

    for pair in data:
        left, right = map(eval, pair)
        print(compare(left, right))


































        # left, right = map(eval, pair)
        # print(left, any([type(e) == list for e in left]))
        # print(right, any([type(e) == list for e in right]))

        # if type(left) == int and type(right) == int: #both integers
        #     if left < right:
        #         print('right order')
        #     else:
        #         print('wrong order')
        # elif type(left) == list and type(right) == list: #both lists

        #     if len(right) > len(left):
        #         print('wrong order')
        #     elif len(right) < len(left):
        #         print('right order')
        #     else:
        #         for i in range(len(left)):
        #             if left[i] < right[i]:
        #                 print('right order')
        #                 break
        #             elif left[i] > right[i]:
        #                 print('wrong order')
        #                 break

        # else: #one integer, one list
        #     left = [left] if type(left) == int else left
        #     left = [right] if type(right) == int else right

        #     if len(right) > len(left):
        #         print('wrong order')
        #     elif len(right) < len(left):
        #         print('right order')
        #     else:
        #         for i in range(len(left)):
        #             if left[i] < right[i]:
        #                 print('right order')
        #                 break
        #             else:
        #                 print('wrong order')
        #                 break




        # # any([type(e) == list for e in left]) == False and any([type(e) == list for e in right]) == False: #both parts lists


    
        # print('====')