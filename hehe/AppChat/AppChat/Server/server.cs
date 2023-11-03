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

namespace Server
{
    public partial class Client : Form
    {
        public Client()
        {
            InitializeComponent();
            CheckForIllegalCrossThreadCalls = false;
            Connect();
        }

        private void Client_FormClosed(object sender, FormClosedEventArgs e)
        {
            Close();
        }

        private void btnSend_Click(object sender, EventArgs e)
        {
            foreach(Socket item in clientList)
            {
                Send(item);
            }
            AddMes(txbMes.Text);
            txbMes.Clear();
            
        }

        IPEndPoint ipEndPoint;
        Socket server;
        List<Socket> clientList;

        //ket noi toi server
        void Connect()
        {

            clientList = new List<Socket>();
            ipEndPoint = new IPEndPoint(IPAddress.Any, 1859);
            server = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            server.Bind(ipEndPoint);
            Thread Listen = new Thread(() =>
            {
                try
                {
                    while (true)
                    {
                        server.Listen(10);
                        Socket client = server.Accept();
                        clientList.Add(client);
                        Thread receive = new Thread(Receive);
                        receive.IsBackground = true;
                        receive.Start(client);
                    }
                }
                catch
                {
                    ipEndPoint = new IPEndPoint(IPAddress.Any, 1859);
                    server = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                }
                
                
            });

            Listen.IsBackground = true;
            Listen.Start();
        }


        //dong ket noi

        void Close()
        {
            server.Close();
        }

        //gui tin
        void Send(Socket client)
        {
            if (client!= null && txbMes.Text != string.Empty)
                client.Send(Buffer(txbMes.Text));
        }



        //nhan tin
        void Receive(object obj)
        {
            Socket client = obj as Socket;
            try
            {
                while (true)
                {
                    byte[] data = new byte[1024];
                    client.Receive(data);

                    string mes = (string)Deserialze(data);
                    foreach (Socket item in clientList)
                    {
                        if (item != null && item != client)
                            item.Send(Buffer(mes));
                    }
                    AddMes(mes);
                }
            }
            catch
            {
                clientList.Remove(client);
                client.Close();
            }

        }

        void AddMes(string s)
        {
            listView1.Items.Add(new ListViewItem() { Text = s });
        }

        // phan manh goi tin de gui len tung segment

        byte[] Buffer(object obj)
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

    }
}
