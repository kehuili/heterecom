import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;


public class TextParser {
	
	// extract data from original file and put to arrayList
	static public ArrayList<String[]> splitFile(File file) throws IOException{
		ArrayList<String[]> list = new ArrayList<String[]>();
		BufferedReader br = null;
		br = new BufferedReader(new FileReader(file));
		String contentLine = br.readLine();
		while(contentLine != null){
			String[] splited = contentLine.split("\\t");
			list.add(splited);
			contentLine = br.readLine();
		}
		br.close();
		return list;
	}
	
	static public HashMap<Integer, MovieNode>  authorList2Table(ArrayList<String[]> list){
		HashMap<Integer, MovieNode> ret = new HashMap<Integer, MovieNode>();
		for(String[] ele : list){
			ret.put(new Integer(ele[0]), new MovieNode(ele[0], ele[1]));
		}
		return ret;
	}
	
	static public HashMap<Integer, ActorNode>  paperList2Table(ArrayList<String[]> list){
		HashMap<Integer, ActorNode> ret = new HashMap<Integer, ActorNode>();
		for(String[] ele : list){
			ret.put(new Integer(ele[0]), new ActorNode(ele[0], ele[1]));
		}
		return ret;
	}
	
	static public HashMap<Integer, GenreNode>  venueList2Table(ArrayList<String[]> list){
		HashMap<Integer, GenreNode> ret = new HashMap<Integer, GenreNode>();
		for(String[] ele : list){
			ret.put(new Integer(ele[0]), new GenreNode(ele[0], ele[1]));
		}
		return ret;
	}
	
	static public HashMap<Integer, DirectorNode>  termList2Table(ArrayList<String[]> list){
		HashMap<Integer, DirectorNode> ret = new HashMap<Integer, DirectorNode>();
		for(String[] ele : list){
			ret.put(new Integer(ele[0]), new DirectorNode(ele[0], ele[1]));
		}
		return ret;
	}
}
