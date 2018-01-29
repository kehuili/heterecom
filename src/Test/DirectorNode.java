
public class DirectorNode extends SimNode{
	private int type;
	
	public DirectorNode(String id, String data){
		super(id, data);
		this.type = 3;
	}
	
	public int getType(){return this.type;}
}
