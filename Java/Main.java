import java.util.ArrayList;

public class Main {
	private static JavaDatabase JD;
	public static void PrintResults(ArrayList<ArrayList<String>> Data) {
		for(int i=0;i<Data.size();++i) {
			for (int j=0;j<Data.get(i).size();++j) {
				System.out.printf(String.format("[%s]", Data.get(i).get(j)));
		} System.out.print("\n"); }
	}
	public static void main(String ars[]) {
		//Creating a connection with the database server
		JD = new JavaDatabase("jdbc:mysql://localhost:3306/database1?allowPublicKeyRetrieval=false&useSSL=false","root","pass"); 
		//Creating new tables
		JD.DDL_DML("create table employees (ID INT NOT NULL, name VARCHAR(255), address VARCHAR(255), Primary Key(ID))");
		JD.DDL_DML("create table managers (ID INT NOT NULL, name VARCHAR(255), address VARCHAR(255), Primary Key(ID))");
		//Inserting some data into tables
		JD.DDL_DML("insert into employees (ID, name, address) Values (0, 'Fred', '555 Pebble Beach Rd'),(1, 'Emily', '123 Summerhill Rd')");
		JD.DDL_DML("insert into managers (ID, name, address) Values (1, 'Emily', '123 Summerhill Rd'),(2, 'Bob', '159 Main St, Apt 56')");
		//Show all data in 'customers' table
		PrintResults(JD.DQL("select * from employees"));
		//Join the two tables to find managers with the same ID as employees
		PrintResults(JD.DQL("select managers.name, managers.address from managers inner join employees on employees.ID = managers.ID"));
		//Dropping all existing tables
		JD.DDL_DML("drop table employees");
		JD.DDL_DML("drop table managers");
		//Closing connection to sql server
		JD.closeConnection();	
		} 
	}