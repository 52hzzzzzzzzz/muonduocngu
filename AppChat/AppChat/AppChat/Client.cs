using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Runtime.Serialization.Formatters.Binary;
using System.Threading;

namespace AppChat
{
    public partial class Client : Form
    {
        public Client()
        {
            InitializeComponent();
            CheckForIllegalCrossThreadCalls = false;
            Connect();
        }

        public bool isExit = true;
        public event EventHandler LogOut;


        private void btnExit_Click(object sender, EventArgs e)
        {
            if (isExit)
                Application.Exit();
        }

        private void Client_FormClosed(object sender, FormClosedEventArgs e)
        {
            Close();
            if(isExit)
            Application.Exit();
        }

        private void Client_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (isExit)
            {
                if (MessageBox.Show("Thoat chuong trinh", "canh bao", MessageBoxButtons.YesNo) != DialogResult.Yes)
                    e.Cancel = true;
            }
        }


        private void btnLogOut_Click(object sender, EventArgs e)
        {
            if (LogOut != null)
            {
                LogOut(this, new EventArgs());
            }
        }

        //xong cac event de tuong tac

        //Bat dau viet chuong trinh chat ket noi client server




        //socket, ip


        IPEndPoint ipEndPoint;
        Socket client;

        //ket noi toi server
         void Connect()
        {
            ipEndPoint = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 1859);
            client = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            try
            {
                client.Connect(ipEndPoint);
            }
            catch
            {
                MessageBox.Show("Khong the conect", "loi", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Thread listen = new Thread(Receive);
            listen.IsBackground = true;
            listen.Start();
        }


        //dong ket noi

        void Close()
        {
            client.Close();
        }

        //gui tin
        void Send()
        {
            
            if(txbMes.Text!= string.Empty)
            client.Send(Buffer("Thong tin duoc gui tu "+ipEndPoint+":"+txbMes.Text));

        }



        //nhan tin
        void Receive()
        {
            try
            {
                while (true)
                {
                    byte[] data = new byte[1024];
                    client.Receive(data);
                    string mes = (string)Deserialze(data);
                    AddMes(mes);
                    
                }
            }
            catch
            {
                Close();
            }
            
        }

        void AddMes(string s)
        {
            listView1.Items.Add(new ListViewItem() { Text = s });
            txbMes.Clear();
        }

        // phan manh goi tin de gui len tung segment

        byte[]  Buffer(object obj)
        {
            MemoryStream stream = new MemoryStream();
            BinaryFormatter formatter = new BinaryFormatter();
            formatter.Serialize(stream, obj);
            return stream.ToArray();
        }

        //nhan segment gom lai

        object Deserialze(byte[] data)
        {
            MemoryStream stream = new MemoryStream(data);
            BinaryFormatter formatter = new BinaryFormatter();
            return formatter.Deserialize(stream);
            
        }
            

        //gui tin nhan len server
        private void btnSend_Click(object sender, EventArgs e)
        {
            Send();
            AddMes(txbMes.Text);
        }
    }
}
