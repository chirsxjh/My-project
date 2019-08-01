package tencentcloud

import (
	"encoding/json"
	"fmt"
	"log"

	//"github.com/zqfan/tencentcloud-sdk-go/services/cvm/v20170312"

	//"github.com/agext/levenshtein"
	"github.com/hashicorp/terraform/helper/schema"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"

	//"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	//"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	clb "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/clb/v20180317"
)



func resourceTencentCloudListener() *schema.Resource {
	return &schema.Resource{
		Create: resourceTencentCloudListenerCreate,
		Read:   resourceTencentCloudListenerRead,
		Update: resourceTencentCloudListenerUpdate,
		Delete: resourceTencentCloudListenerDelete,


		Schema: map[string]*schema.Schema{
			"load_balancer_id": {
				Type:     schema.TypeString,
				Required: true,
				ForceNew: true,
			},

			"frontend_port": {
				Type:     schema.TypeInt,
				Required: true,
			},
			"backend_port": {
				Type:     schema.TypeInt,
				Required: true,
			},

			//"frontend_port": {
			//	Type:         schema.TypeInt,
			//	Required:     true,
			//	ForceNew:     true,
			//},
			//"load_balancer_port": {
			//	Type:       schema.TypeInt,
			//	Optional:   true,
			//	//Deprecated: "Field 'lb_port' has been deprecated, and using 'frontend_port' to replace.",
			//},

			//"backend_port": {
			//	Type:         schema.TypeInt,
			//	Optional:     true,
			//	ForceNew:     true,
			//},

			//"instance_port": {
			//	Type:       schema.TypeInt,
			//	Optional:   true,
			//	//Deprecated: "Field 'instance_port' has been deprecated, and using 'backend_port' to replace.",
			//},



			"protocol": {
				Type:       schema.TypeString,
				Required: true,

			},


			"listener_names": {
				Type:         schema.TypeString,
				Optional:     true,
			},

			"time_out": {
				Type:             schema.TypeInt,
				Optional:         true,

			},

			"http_check_domain": {
				Type:             schema.TypeString,
				Optional:         true,

			},

			"http_code": {
				Type:             schema.TypeInt,
				Optional:         true,

			},

			"interval_time": {
				Type:             schema.TypeInt,
				Optional:         true,

			},



			//http & https
			"health_check": {
				Type:             schema.TypeInt,
				Optional:         true,

			},

			//"health_check_type": {
			//	Type: schema.TypeString,
			//	Optional:         true,
			//},

			"health_check_domain": {
				Type:             schema.TypeString,
				Optional:         true,

			},

			"health_switch": {
				Type:             schema.TypeInt,
				Optional:         true,
				Default:          "1",
			},

			"http_check_path": {
				Type:             schema.TypeString,
				Optional:         true,
				Default:          "/",
			},

			//"health_check_connect_port": {
			//	Type:             schema.TypeInt,
			//	Optional:         true,
			//	Computed:         true,
			//},
			//tcp
			//"ssl_certificate_id": {
			//	Type:             schema.TypeString,
			//	Optional:         true,
			//},
			//http & https & tcp


			"ssl_certificate_id": {
				Type:             schema.TypeString,
				Optional:         true,
				//DiffSuppressFunc: sslCertificateIdDiffSuppressFunc,
			},
			"sessionexpiretime": {
				Type:             schema.TypeInt,
				Optional:         true,
			},

			//http & https & tcp
			"scheduler": {
				Type:             schema.TypeString,
				Optional:         true,
				Default:          "WRR",
			},
			"sniswitch": {
				Type:             schema.TypeInt,
				Optional:         true,
			},

		},
	}
}

func resourceTencentCloudListenerCreate(d *schema.ResourceData, meta interface{}) error {

	client := meta.(*TencentCloudClient).clbConn
	healthCheck:=getListenerParams(client,d)
	req := clb.NewCreateListenerRequest()
	data, err := json.Marshal(healthCheck)
	err = req.FromJsonString(string(data))
	if err != nil {
		panic(err)
	}

	resp, err := client.CreateListener(req)

    writeToFile("CreateListener",req)
    writeToFile("resp",resp)

	if err != nil {
		return err
	}

	fmt.Printf("%s", resp.ToJsonString())
	d.SetId(*resp.Response.ListenerIds[0])

	return resourceTencentCloudListenerRead(d, meta)








}

func  resourceTencentCloudListenerRead(d *schema.ResourceData, meta interface{}) error {
	client := meta.(*TencentCloudClient).clbConn
	lbid :=d.Get("load_balancer_id")
	params := map[string]interface{}{}
	params["LoadBalancerId"] = lbid
	req := clb.NewDescribeListenersRequest()
	data, err := json.Marshal(params)
	log.Printf("[DEBUG] dataSourceTencentCloudListenersRead read params:%v", data)

	err = req.FromJsonString(string(data))
	resp, err := client.DescribeListeners(req)
	if err != nil {
		log.Printf("[ERROR] resourceTencentCloudListenerRead read client.SendRequest error:%v", err)
		return err
	}

	if len(resp.Response.Listeners) == 0 {
		d.SetId("")
		return nil
	}
	//healthckeck := resp.Response.Listeners[0].HealthCheck
	//httpCheckDomain := healthckeck.HttpCheckDomain
	//if len(httpCheckDomain) > 0 {
	//	d.Set("http_check_domain", httpCheckDomain)
	//}
	////healthSwitch := *healthckeck.HealthSwitch
	////if healthSwitch {
	////	d.Set("http_check_domain", healthSwitch)
	////}
	//
	//httpCheckPath := *healthckeck.HttpCheckPath
	////http_check_path
	//if len(httpCheckPath) > 0 {
	//	d.Set("http_check_path", httpCheckPath)
	//}
	////HealthCheck *HealthCheck


	Protocol := resp.Response.Listeners[0].Protocol
	d.Set("protocol",Protocol )

	ListenerId := resp.Response.Listeners[0].ListenerId
	d.Set("listener_id",ListenerId )


	Port := resp.Response.Listeners[0].Port
	d.Set("port",Port )

	Scheduler := resp.Response.Listeners[0].Scheduler
	d.Set("scheduler",Scheduler )

	SessionExpireTime := resp.Response.Listeners[0].SessionExpireTime
	d.Set("sessionexpireTime",SessionExpireTime )

	SniSwitch := resp.Response.Listeners[0].SniSwitch
	d.Set("sniswitch",SniSwitch )

	ListenerName := resp.Response.Listeners[0].ListenerName
	d.Set("listenername",ListenerName )


	//var ruleList []map[string]interface{}
	//rules := resp.Response.Listeners[0].Rules
	//for _, rule := range rules {
	//	m := make(map[string]interface{})
	//	sessionexpiretime := rule.SessionExpireTime
	//	listenerid := rule.ListenerId
	//	scheduler := rule.Scheduler
	//	domain := rule.Domain
	//	url := rule.Url
	//	locationid := rule.LocationId
	//	m["sessionexpiretime"] = diskType
	//	m["data_disk_size"] = diskSize
	//	dataDiskList = append(dataDiskList, m)
	//}
	//d.Set("data_disks", dataDiskList)





	//err := req.FromJsonString(params)
	//if err != nil {
	//	panic(err)
	//}
	//
	//if err != nil {
	//	return err
	//}
	//
	//d.Set("listenerids", *resp.Response.Listeners[0])
	//d.Set("portocol", *resp.Response.Listeners[1])
	//d.Set("port", *resp.Response.Listeners[2])
	//d.Set("listener_names",*resp.Response.Listeners[9])
	//d.Set("certificate ", *resp.Response.Listeners[3] )
	//d.Set("sessionexpiretime ", *resp.Response.Listeners[6])
	//d.Set("scheduler ", *resp.Response.Listeners[5])
	//d.Set("health_check", *resp.Response.Listeners[4])
	//d.Set("sniswitch", *resp.Response.Listeners[7])
	writeToFile("CreateListenerread",req)
	writeToFile("respread",resp)
	return nil


}

func resourceTencentCloudListenerUpdate(d *schema.ResourceData, meta interface{}) error {

	client := meta.(*TencentCloudClient).clbConn
	ListenerId := d.Id()
	req := clb.NewModifyListenerRequest()
	params := map[string]interface{}{}
	params["LoadBalancerId"] = d.Get("load_balancer_id")
	params["ListenerId"] = &ListenerId
	data, err := json.Marshal(params)
	err = req.FromJsonString(string(data))
	//req.LoadBalancerId = common.StringPtr(d.Get("load_balancer_id").(string))
	//req.ListenerId  = &ListenerId
    //params["LoadBalancerId"] = d.Get("load_balancer_id")
    //params["ListenerId"] = &ListenerId
	//params := fmt.Sprintf("{'LoadBalancerId ':'%s','ListenerId':'%s' }",req.LoadBalancerId, req.ListenerId )

	//err := req.FromJsonString(params)

	if err != nil {
		panic(err)
	}

	resp, err := client.ModifyListener(req)

	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return nil
	}

	if err != nil {
		return err
	}
	fmt.Printf("%s", resp.ToJsonString())


	if !d.HasChange("listener_names") {
		return nil
	}
	if !d.HasChange("load_balancer_id") {
		return nil
	}

	if !d.HasChange("frontend_port") {
		return nil
	}

	if !d.HasChange("backend_port") {
		return nil
	}

	if !d.HasChange("time_out") {
		return nil
	}



	if !d.HasChange("protocol") {
		return nil
	}
	if !d.HasChange("http_code") {
		return nil
	}


	if !d.HasChange("interval_time") {
		return nil
	}


	if !d.HasChange("health_check_domain") {
		return nil
	}

	if !d.HasChange("health_switch") {
		return nil
	}


	if !d.HasChange("http_check_path") {
		return nil
	}


	if !d.HasChange("health_check") {
		return nil
	}

	if !d.HasChange("ssl_certificate_id") {
		return nil
	}

	if !d.HasChange("sessionexpiretime") {
		return nil
	}

	if !d.HasChange("scheduler") {
		return nil
	}

	if !d.HasChange("sniswitch") {
		return nil
	}

	return resourceTencentCloudListenerRead(d, meta)
}

func resourceTencentCloudListenerDelete(d *schema.ResourceData, meta interface{}) error {
	client := meta.(*TencentCloudClient).clbConn
	params := map[string]interface{}{}
	Listenerid := d.Id()
	req := clb.NewDeleteListenerRequest()
	//req.ListenerId  = &Listenerid
	//req.LoadBalancerId = common.StringPtr(d.Get("load_balancer_id").(string))
    params["LoadBalancerId"] = d.Get("load_balancer_id")
    params["ListenerId"] = &Listenerid

	data, err := json.Marshal(params)
	err = req.FromJsonString(string(data))
	//params := fmt.Sprintf("{'LoadBalancerId ':'%s','ListenerId':'%s' }",req.LoadBalancerId, req.ListenerId )
	//err := req.FromJsonString(params)
	if err != nil {
		return err
	}

	resp, err := client.DeleteListener(req)

	fmt.Printf("%s", resp.ToJsonString())

	if err != nil {
		return err
	}


	d.SetId("")
	return nil
}


func getListenerParams(client *clb.Client,d *schema.ResourceData) map[string]interface{} {
	params := map[string]interface{}{}
	HealthCheck := map[string]interface{}{}
	CertificateInput := map[string]interface{}{}

	params["HealthCheck"] = HealthCheck
	params["CertificateInput"] = CertificateInput
	//params["SessionExpireTime"] = d.Get("sessionexpiretime")

	//此处为必填参数
	params["LoadBalancerId"] = d.Get("load_balancer_id")
	params["Protocol"] = d.Get("protocol")


	//params["SniSwitch"] = d.Get("sniswitch")




	//端口号
	frontendPort := d.Get("frontend_port").(int)
	backendPort := d.Get("backend_port").(int)
	port := []int{}
	port = append(port, frontendPort, backendPort)
	params["Ports"] = port


	//权重轮询
	SniSwitch,SniSwitchok := d.GetOk("sniswitch")
	if SniSwitchok{
		params["SniSwitch"] = SniSwitch

	}


	//权重轮询
	Scheduler,Schedulerok := d.GetOk("scheduler")
	if Schedulerok{
		params["scheduler"] = Scheduler

	}

	//会话保持时间
	SessionExpireTime,SessionExpireTimeok := d.GetOk("sessionexpiretime")
	if SessionExpireTimeok{
		params["SessionExpireTime"] = SessionExpireTime

	}
   //监听器名称
    ListenerName,ListenerNameok := d.GetOk("listener_names")
	if ListenerNameok{
		params["ListenerNames"] = ListenerName

	}


   //此处为Certificate结构体
	SslCertificateId, SslCertificateIdok := d.GetOk("ssl_certificate_id")
	if SslCertificateIdok{
		CertificateInput["ssl_certificate_id"]=SslCertificateId
	}



   //此处为healthcheck结构体
	HealthSwitch, HealthSwitchok := d.GetOk("health_switch")
	if HealthSwitchok{
		HealthCheck["health_switch"]=HealthSwitch
	}

	HealthNum, HealthNumok := d.GetOk("health_num")
	if HealthNumok{
		HealthCheck["health_num"]=HealthNum
	}


	TimeOut, TimeOutok := d.GetOk("time_out")
	if TimeOutok{
		HealthCheck["time_out"]=TimeOut

	}

	HttpCode, HttpCodeok := d.GetOk("http_code")
	if HttpCodeok{
		HealthCheck["http_code"]=HttpCode

	}


	HttpCheckDomain, HttpCheckDomainok := d.GetOk("health_checkmethod")
	if HttpCheckDomainok{
		HealthCheck["health_checkmethod"]=HttpCheckDomain

	}

	IntervalTime, IntervalTimeok := d.GetOk("interval_time")
	if IntervalTimeok{
		HealthCheck["interval_time"]=IntervalTime

	}

	HttpCheckPath, HttpCheckPathok := d.GetOk("http_check_path")
	if HttpCheckPathok{
		HealthCheck["http_check_path"]=HttpCheckPath

	}


	return params
}
