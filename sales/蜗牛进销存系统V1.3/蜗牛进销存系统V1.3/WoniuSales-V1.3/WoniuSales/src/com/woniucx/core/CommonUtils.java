package com.woniucx.core;

import java.io.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import jxl.Cell;
import jxl.Sheet;
import jxl.Workbook;

public class CommonUtils {

	public static String generateDateTime(String format) {
		SimpleDateFormat formatter = 
				new SimpleDateFormat(format);
		Date date = new Date();
		String now = formatter.format(date.getTime());
		return now;
	}
	
	public static String[][] readExcel(String fileName){
		File file = new File(fileName);
		String[][] data = null; 
	    try{
	        FileInputStream fis = new FileInputStream(file); 
	        jxl.Workbook rwb = Workbook.getWorkbook(fis);
	       
	        Sheet sheet = rwb.getSheets()[0];
	        // 获取到sheet中的行和列总数量，用于定义二维数组
	        int rowCount = sheet.getRows();
	        int colCount = sheet.getColumns();
	        // 默认情况下，第一行定义列名，所以数据内容应该会少一行
	        data = new String[rowCount-1][colCount];
	        
	        // 遍历表格中的行和列，并赋值给data数组
	        // 循环从i=1开始，是为了绕开表格中的第一行
	        for (int i=1; i<rowCount; i++) {   
	           Cell[] cells = sheet.getRow(i);
	           // 遍历当前行中的每一列，第赋值给data数组
	           for(int j=0; j<cells.length; j++) { 
	        	   data[i-1][j] = cells[j].getContents();
	           }
	        }  
	        fis.close();
	    }catch(Exception e){
	        System.out.println(e.getMessage());
	    }
	    return data;
	}
}
