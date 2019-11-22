import java.sql.*;
import java.util.ArrayList;

public class JavaDatabase {
	private static Connection Conn;
	JavaDatabase(String URL, String User, String Pass) {
		try  {
			Conn = DriverManager.getConnection(URL,User,Pass);
   		 	System.out.println("Database connected!");
		} catch (SQLException e) {
    		throw new IllegalStateException("Cannot connect the database!", e);
		}
	}
	public void closeConnection() {
		try {
			Conn.close();
		} catch(Exception e) { /*Ignored*/ }
	}
	public boolean DDL_DML(String D) {
		try {
			Statement Stmt = Conn.createStatement();
			Stmt.executeUpdate(D); 
		} catch(SQLException e) {
			e.printStackTrace();
			return false;
		} return true;
	}
	public ArrayList<ArrayList<String>> DQL(String Q) {
		ArrayList<ArrayList<String>> TR = new ArrayList<ArrayList<String>>();
		try {
			Statement Stmt = Conn.createStatement();
			ResultSet RS = Stmt.executeQuery(Q);
			ResultSetMetaData RSMD = RS.getMetaData();
			while (RS.next()) {
				TR.add(new ArrayList<String>());
				for(int i=1;i<RSMD.getColumnCount()+1;++i)
					TR.get(RS.getRow()-1).add(RS.getString(i)); 
			} RS.close(); return TR;
		} catch(SQLException e) {
			e.printStackTrace();
			return null;
		}}
	}