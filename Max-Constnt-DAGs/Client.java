package BacjUp;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Map;
import java.util.Set;

public class Client {

	public static String root="1";
	static int count=0;
	static int totalCount=0;
	
	public static HashSet<HashSet> totalDAG=new HashSet<HashSet>();
	public static Map readNodes=new HashMap<String, HashSet<HashSet>>();
	static HashMap<String, LinkedHashSet<String>> parentChild=new HashMap<String, LinkedHashSet<String>>();
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashMap<String, HashSet<String>> childParentHM=new HashMap<String, HashSet<String>>();
		LinkedList<String> queueLinkedList=new LinkedList<String>();	
      	LinkedHashMap<String, HashSet> linkedHashMap=new LinkedHashMap<String,HashSet>();		
		//String fileName = "C:/VK/alog/src/miniProject/min-imfo.txt";
		String rootFile = "C:/VK/alog/src/miniProject/mfo_names.txt";
		String givenEdgesFile = "C:/VK/alog/src/miniProject/created_File.txt";
		FileReader fileReader;
	     BufferedReader bufferedReader;
	     
	     
	      
	     try {
	    	 FileReader filereader2=new FileReader(rootFile);
	      	 
	       	bufferedReader = new BufferedReader(filereader2);
	       	String line = null;
	       	 

	       	 while((line = bufferedReader.readLine()) != null) 
	       	 {
	                 if(line.indexOf("_")!=-1)
	                 	//root=line.substring(line.indexOf("GO:")+3,line.indexOf(" "));
	                      root=line.substring(line.indexOf("GO:")+3,line.indexOf("\t")).trim();
	       	 }
	       	 root="1";
	       	
	     System.out.println("Root: "+ root);
	     fileReader = new FileReader(givenEdgesFile);
      	 bufferedReader = new BufferedReader(fileReader);
      	 String key;
         String value;
        
      	 while((line = bufferedReader.readLine()) != null) 
      	 {
                
                if(line.indexOf("GO:")==-1)
                	continue;
                key=line.substring(line.indexOf("GO:")+3,line.indexOf("\t")).trim();
                value=line.substring(line.lastIndexOf("GO:")+3,line.length()).trim();
                if(childParentHM.get(key)==null)
                {
                	
                	HashSet<String> tempHashSet = new HashSet<String>();
                	if(value.equals(root))
                	{
                		queueLinkedList.add(key);
                	}
                	tempHashSet.add(value);
                	childParentHM.put(key, tempHashSet);
                }
                else
                {
                	HashSet<String> tempHashSet = new HashSet<String>();
                	tempHashSet=childParentHM.get(key);
                	tempHashSet.add(value);
                }
                
                if(parentChild.get(value)==null)
                {
                	
                	LinkedHashSet<String> tempLinkedList = new LinkedHashSet<String>();
                	tempLinkedList.add(key);
                	parentChild.put(value, tempLinkedList);
                }
                else
                {
                	LinkedHashSet<String> tempHashSet = new LinkedHashSet<String>();
                	tempHashSet=parentChild.get(value);
                	tempHashSet.add(key);
                }
         }
      	 
		while(!queueLinkedList.isEmpty())
		{
			 int sizeLinkedList=queueLinkedList.size();
			 while(sizeLinkedList!=0)
			 {
				 HashSet tempHS=(HashSet)parentChild.get(queueLinkedList.get(0));
				 if(tempHS!=null)
				 {
		  		 Iterator iteratorHashSet=tempHS.iterator();
		  		 while(iteratorHashSet.hasNext())
		  		 {
		  			 String nextElement=(String)iteratorHashSet.next();
		  			queueLinkedList.addLast(nextElement);
		      	 }
		  		sizeLinkedList--;
		  		 
		  		linkedHashMap.put((String)queueLinkedList.getFirst(),childParentHM.get(queueLinkedList.getFirst()) );
		  		queueLinkedList.remove(0);
		  		 
		  	 }
				 else
				 {
					 linkedHashMap.put((String)queueLinkedList.getFirst(),childParentHM.get(queueLinkedList.getFirst()) );
					 sizeLinkedList--;
					 queueLinkedList.remove(0);
				 }
			 }
		}
      	bufferedReader.close();
      	System.out.println("Numder of nodes: "+childParentHM.size());
      	printMap(childParentHM);
      	System.out.println("------------");
      	//printMap(linkedHashMap);
      	//childParentHM.clear();
      	parentChild.clear();
      	calConsistentDAG(linkedHashMap,root);
      	int totalDAGcount=totalDAG.size()+1;
      	System.out.println("TotalSize: "+totalDAGcount);
      /*	Iterator toRecieve = hsPublic.iterator();
      	while(toRecieve.hasNext())
      	{
      		System.out.println(toRecieve.next());
      	}*/
      	
	     }
	 	catch(FileNotFoundException ex) {
            System.out.println("Unable to open file '" + "" + "'");                
     	}
        catch(IOException ex) {
            System.out.println("Error reading file '"+ "" + "'");                  
        }
        catch(Exception ex) {
            System.out.println("Error " + ex.getMessage() + "'");
            ex.printStackTrace();
            
        }
	}

	
	public static void calConsistentDAG(Map m,String root)
	{
		Iterator it = m.entrySet().iterator();
		String value="";
		int count=0;
	    while (it.hasNext()) 
	    {
	    	Map.Entry pair = (Map.Entry)it.next();
	        value=(String)pair.getKey();
	        if(readNodes.get(value)==null)
	        {
	        	addElement(m,value,count);
	        }
	        
	    }
	}

private static HashSet<String> addElement(Map m, String key,int count) {
		// TODO Auto-generated method stub
		Iterator it = m.entrySet().iterator();
		HashSet<String> allParents=new HashSet<String>();
		HashSet<String> newNodeHS=new HashSet<String>();
		HashSet<String> receive=new HashSet<String>();
		String parent="";
		if(readNodes.get(key)==null)
		{
			if(!(key.equals(root)))
			{
			allParents=(HashSet)m.get(key);
			Iterator iter = allParents.iterator();
			while(iter.hasNext())
			{
				parent=(String)iter.next();
				count++;
				receive=addElement(m,parent,count);
				String str=key+"-"+parent;
				Iterator toRecieve = receive.iterator();
				while(toRecieve.hasNext())
				{
					newNodeHS.add((String)toRecieve.next());
				}
				newNodeHS.add(str);
				count--;
			}
				if(count==0)
				{
					Iterator<HashSet> iternew = totalDAG.iterator();
					HashSet<HashSet> inProgressDAG=new HashSet<HashSet>(totalDAG); 
					while (iternew.hasNext()) {
					    HashSet<String> tillCreatedDAG=iternew.next();
					    HashSet<String> union=new HashSet<String>(newNodeHS);
					    union.addAll(tillCreatedDAG);
					    inProgressDAG.add(union);
					}
					totalDAG.clear();
					totalDAG=inProgressDAG;
					totalDAG.add(newNodeHS);
					readNodes.put(key, newNodeHS);
					System.out.println("Size: " +totalDAG.size()+" Nodes: "+(++totalCount));
					return newNodeHS;
				}
				count--;
				return newNodeHS;	
				}	
				else
				{
					String str=root;
					newNodeHS.add(str);
					count--;
					return newNodeHS;
				}
		}
		else
		{
			return (HashSet)readNodes.get(key);
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
	
	public String readFile(String str) {
		// TODO Auto-generated method stub
		 FileReader fileReader;
	     BufferedReader bufferedReader;
	     StringBuilder text=new StringBuilder();
	     
	     try {
	     fileReader = new FileReader(str);
       	 bufferedReader = new BufferedReader(fileReader);
       	 String line = null;

       	 while((line = bufferedReader.readLine()) != null) 
       	 {
                 text.append(line+"\n");
         }  
       	bufferedReader.close();
	     }
	     	catch(FileNotFoundException ex) {
	            System.out.println("Unable to open file '" + str + "'");                
	     	}
	        catch(IOException ex) {
	            System.out.println("Error reading file '"+ str + "'");                  
	        }
	        catch(Exception ex) {
	            System.out.println("Error " + ex.getMessage() + "'");
	            ex.printStackTrace();
	            
	        }
	     
		return text.toString();
	}

	
}
