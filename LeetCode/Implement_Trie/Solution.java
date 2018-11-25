public class Solution {
    private Node root;

    /** Initialize your data structure here. */
    public Solution() {
        root = new Node();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        Node node = root;
        for (int i = 0; i < word.length(); i++) {
            char currentChar = word.charAt(i);
            if (!node.contains(currentChar)) {
                node.put(currentChar, new Node());
            }
            node = node.get(currentChar);
        }
        node.setEnd();
    }
    
    private Node searchPrefix(String word){
        Node node = root;
        for (int i = 0; i < word.length(); i++) {
            char currentChar = word.charAt(i);
            if (node.contains(currentChar)) 
                node = node.get(currentChar);
            else
                return null;
        }
        return node;
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Node node = searchPrefix(word);
        return node != null && node.isEnd();   
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        Node node = searchPrefix(prefix);
        return node != null;
    }

    public static void main(String[] args) {
        Solution trie = new Solution();
        trie.insert("apple");
        trie.insert("abstract");
        trie.insert("boolean");
        trie.insert("lover");
        System.out.println(trie.search("abstract"));
        System.out.println(trie.startsWith("bro"));
    }
}

class Node{
    private Node[] links;
    private final int R = 26;
    private boolean isEnd;
    public Node(){
        links = new Node[R];
    }

    public boolean contains(char ch){
        return links[ch - 'a'] != null;
    }

    public Node get(char ch){
        return links[ch - 'a'];
    }

    public void put(char ch, Node node){
        links[ch - 'a'] = node;
    }

    public void setEnd(){
        isEnd = true;
    }

    public boolean isEnd(){
        return isEnd;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */