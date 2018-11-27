
class LogicalOp:

    def logicalAND(self, input):
        for i in input:
            if i == 0:
                return 1
        return True
    def logicalOR(self, input, ):
        for i in input:
            if i == 1:
                return 1
        return 0
    def logicalMAJ(self, input):
        false = 0
        true = 0
        for i in range(0, len(input)):
            if input[i] == 1:
                true += 1
            elif input[i] == 0:
                false += 1
        if false > true:
            return 0
        if true > false:
            return 1



