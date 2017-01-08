package singleParentTreeMP;

import java.math.BigInteger;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;


public class Client {

	static HashMap<String, String> childParent=new HashMap<String, String>();
    static HashMap<String, HashSet<String>> parentChild=new HashMap<String, HashSet<String>>();
  	static HashMap<String,Long> occurences=new HashMap<String,Long>();
  	static String root="1";
  	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//String filename="C:/VK/alog/src/miniProject/tree_25.txt";
		String givenEdgesFile="C:/Users/Vikrant Kaushal/Downloads/data/dag10-2.txt";
		String createdFile="C:/VK/alog/src/miniProject/created_file.txt";
		
		
		try
		{
			FileReader fileReader=new FileReader(givenEdgesFile);
			
			BufferedReader br=new BufferedReader(fileReader);
			String line;
			int countRow=0;
			HashMap<Integer,Integer> obj=new HashMap<Integer,Integer>();
			HashSet<Integer> value=new HashSet<Integer>();
			while((line=br.readLine())!=null)
			{
				++countRow;
				String[] arr=line.split(" ");
				int length=arr.length;
				for(int i=0;i<length;i++)
				{
					if((new Integer(arr[i]))==1)
					{
						obj.put(i+1, countRow);
					}
				}
			}
			
			Iterator it = obj.entrySet().iterator();
			File file = new File("C:/VK/alog/src/miniProject/created_File.txt");
            file.createNewFile();
            FileWriter fw = new FileWriter(file);
            BufferedWriter bw = new BufferedWriter(fw);
            
            
		    while (it.hasNext()) 
		    {
		        Map.Entry pair = (Map.Entry)it.next();
		        //System.out.println("GO:"+pair.getKey() + "\t" + "GO:"+pair.getValue());
		        bw.write("GO:"+pair.getKey() + "\t" + "GO:"+pair.getValue());
		        bw.newLine();
		    }
		    bw.flush();
		    br.close();
            bw.close();
		}
		catch(IOException ex)
		{
			System.out.println("Exception: "+ex.getMessage());
			ex.printStackTrace();
		}
		
		
		
		try
		{
			FileReader fileReader1=new FileReader(createdFile);
			BufferedReader br1=new BufferedReader(fileReader1);
			String line;
			String key;
	        String value;
	        StringBuilder text=new StringBuilder();
	         while((line = br1.readLine()) != null) 
	      	 {
	                text.append(line+"\n");
	                if(line.indexOf("GO:")==-1)
	                	continue;
	                key=line.substring(line.indexOf("GO:")+3,line.indexOf("\t"));
	                value=line.substring(line.lastIndexOf("GO:")+3,line.length());
	                if(childParent.get(key)==null)
	                {
	                	childParent.put(key, value);
	                }
	                if(parentChild.get(value)==null)
	                {
	                	
	                	HashSet<String> test = new HashSet<String>();
	                	test.add(key);
	                	parentChild.put(value, test);
	                }
	                else
	                {
	                	HashSet<String> test = new HashSet<String>();
	                	test=parentChild.get(value);
	                	test.add(key);
	                }
	         }
	      	//printMap(childParent);
	      	//System.out.println("----------------------");
	      	//printMap(parentChild);
	      	int rootChildCount=countRootChildren(parentChild, root);
	      	HashSet<String> rootChild=(HashSet<String>)parentChild.get(root);
	      
	      	
	      	Iterator iter= rootChild.iterator();
	      	while(iter.hasNext())
	      	{
	      		String child=(String)iter.next();
	      		occurences.put(child, 1L);
	      		if(parentChild.get(child)!=null)
	      		{
	      			calculateDAG(child);
	      		}
	      	}
	      	long totalDAG=0;
	      	Iterator iter1= rootChild.iterator();
	      	if(rootChildCount>1)
	      	{
	      		long firstChildCount=occurences.get(iter1.next());
	      		long secondChildCount=occurences.get(iter1.next());
	      		totalDAG=(long)firstChildCount+firstChildCount*secondChildCount+secondChildCount;
	      	}
	      	BigInteger sum = BigInteger.valueOf(totalDAG);
	      	while(iter1.hasNext())
	      	{
	      		long next=occurences.get(iter1.next());
	      		BigInteger nextBig = BigInteger.valueOf(next);
	      		BigInteger multiply=sum.multiply(nextBig);
	      		sum=sum.add(multiply);
	      		sum=sum.add(nextBig);
	      		totalDAG=(long)totalDAG+totalDAG*next+next;
	      		}
	      	totalDAG+=1;
	      	BigInteger one = BigInteger.valueOf(1);
	      	sum=sum.add(one);
	      	System.out.println("---------------------------------------");
	      	System.out.println("Total consistent DAG: "+sum);
	      	br1.close();
	    }
		catch(IOException ex)
		{
			System.out.println("Exception: "+ex.getMessage());
			ex.printStackTrace();
		}
		
	}
	
	public static void calculateDAG(String root)
	{
		HashSet<String> children=new HashSet<String>();
		children=parentChild.get(root);
		Iterator iter=children.iterator();
		while(iter.hasNext())
		{
			String newNode=(String)iter.next();
			long occurencesOfRoot=occurences.get(root);
			occurences.put(newNode, occurencesOfRoot);
			occurences.put(root,occurencesOfRoot*2);
			if(!((String)childParent.get(root)).equals(singleParentTreeMP.Client.root))
			{
				updateOccurences(occurencesOfRoot,root);
			}
			
			if(parentChild.get(newNode)!=null)
			{
				calculateDAG(newNode);
			}
		}
	}
	
	public static void updateOccurences(long occurencesOfRoot,String root)
	{
		String parent=childParent.get(root);
		occurences.put(parent,occurences.get(parent)+occurencesOfRoot);
		if(!(childParent.get(parent).equals(Client.root)))
		{
			updateOccurences(occurencesOfRoot, parent);
		}
	}
	
	
	public static void printMap(Map mp) {
	    Iterator it = mp.entrySet().iterator();
	    while (it.hasNext()) 
	    {
	        Map.Entry pair = (Map.Entry)it.next();
	        System.out.println(pair.getKey() + " = " + pair.getValue());
	    }
	}
	
	public static int countRootChildren(Map m,String root)
	{
		HashSet<String> countChild=(HashSet)m.get(root);
		return countChild.size();
	}

		

	

}
