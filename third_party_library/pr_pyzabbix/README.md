脚本一般都在 zabbix 的 alertscripts 目录（一般在 /usr/lib/zabbix/）

chmod a+x alert.py
chown -R zabbix:zabbix alert.py
./alert.py --init http://localhost/zabbix/api_jsonrpc.php Admin zabbix
