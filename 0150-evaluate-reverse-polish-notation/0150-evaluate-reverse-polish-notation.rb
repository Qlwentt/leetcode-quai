# @param {String[]} tokens
# @return {Integer}
def eval_rpn(tokens)
    operations = {
        "+" => lambda { |a, b| a + b },
        "-" => lambda { |a, b| a - b },
        "*" => lambda { |a, b| a * b },
        "/" => lambda { |a, b| (a.to_f/b).to_i},
    }
    stack = []
    tokens.each do |str|
        if operations[str]
            b = stack.pop
            a = stack.pop

            stack.push(operations[str].call(a,b))
        else
            stack.push(str.to_i)
        end
    end

    return stack.pop
end