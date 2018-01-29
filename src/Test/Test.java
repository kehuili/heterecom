import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.csvreader.*;
public class Test{
	public static void main(String[] args) throws IOException {
//		List<Map<Integer, Integer>> idtonew = new ArrayList<Map<Integer, Integer>>();
		List<Integer> oldid = new ArrayList<Integer>();
		List<Integer> newid = new ArrayList<Integer>();
		CsvReader r1 = new CsvReader("F://bysj//movielens//moviesV.csv");
		CsvReader r2 = new CsvReader("F://bysj//movielens//moviesE.csv");
		CsvWriter w1 = new CsvWriter("F://bysj//movielens//v.csv");
		CsvWriter w2 = new CsvWriter("F://bysj//movielens//e.csv");
	
		String[] content1 = {"id","title","type"};
		String[] content2 = {"id","start","end"};

		w1.writeRecord(content1);
		w2.writeRecord(content2);
		
		r1.readHeaders();
		r2.readHeaders();
		int a = 0;
		int b = 0;
		int c = 0;
		int d = 0;
		while(r1.readRecord()){
			String id = r1.get("id");
			String title = r1.get("title");
			String type = r1.get("type");
			oldid.add(Integer.parseInt(id));
			
			int n = 1;
			int kkk = 0;
			if(type.equals("movie")) {
				n = 1;
				kkk = a;
				a++;
			}else if(type.equals("actor")) {
				n = 70000;
				kkk = b;
				b++;
			}else if(type.equals("director")) {
				n = 170000;
				kkk = c;
				c++;
			}else {
				n = 180000;
				kkk = d;
				d++;
			}
			Integer temp = kkk+n;
			newid.add(temp);
			String[] contents = {temp.toString(), title, type};
			w1.flush();
			w1.writeRecord(contents);
		}
		while(r2.readRecord()){
			String id = r2.get("id");
			String start = r2.get("start");
			String end = r2.get("end");
			
			Integer sss = Integer.parseInt(start);
			Integer eee = Integer.parseInt(end);
			int qqq = oldid.indexOf(sss);
			int ppp = oldid.indexOf(eee);
			
			String[] contents = {id, newid.get(qqq).toString(), newid.get(ppp).toString()};
			w2.flush();
			w2.writeRecord(contents);
		}
		

	}
}
