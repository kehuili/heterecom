
public class ActorNode extends SimNode{
	private int type;
	
	public ActorNode(String id, String data){
		super(id, data);
		this.type = 1;
	}
	
	public int getType(){return this.type;}
}
