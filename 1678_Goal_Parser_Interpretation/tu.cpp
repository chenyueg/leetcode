class Solution {
public:
    string interpret(string command) {
        while(command.find("()")!=std::string::npos)
            command.replace(command.find("()"), sizeof("()") - 1, "o");
        while(command.find("(al)")!=std::string::npos)
            command.replace(command.find("(al)"), sizeof("(al)") - 1, "al");
        return command;
    }
};