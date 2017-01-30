package interview;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

public class BalancedParentheses {
    
    public static boolean isBalanced(String expression) {
        Stack<Character> stack1= new Stack<Character>();
       List<Character> openingSymbol=new ArrayList<Character>();

       
       Map<Character,Character> map=new HashMap<Character, Character>();
       map.put('(', ')');
       map.put('[', ']');
       map.put('{','}');
       
        int size=expression.length()-1;
        Character symbol=null;
        Character match=null;
        boolean flag=true;
        for(int i=0;i<=size;i++){
        	symbol=expression.charAt(i);
        	if (symbol =='[' || symbol == '(' || symbol=='{')
        		stack1.push(symbol);
        	else if (stack1.size()>0 && (symbol ==']' || symbol == ')' || symbol=='}')){
        		match=stack1.pop();
        		if(map.get(match)!=symbol){
        			flag=false;
        			break;
        		}
        	}
        }
        if(stack1.size()>0){
        	flag=false;
        }
        return flag;
    }
  
    public static void main(String[] args) {
    	 
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            String expression = in.next();
            System.out.println( (isBalanced(expression)) ? "YES" : "NO" );
        }
    }
}