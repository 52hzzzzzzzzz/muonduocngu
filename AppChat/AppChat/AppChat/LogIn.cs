using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AppChat
{
    public partial class LogIn : Form
    {
        public LogIn()
        {
            InitializeComponent();
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void btnLogIn_Click(object sender, EventArgs e)
        {
            string userName = txtUsername.Text;
            string passWord = txtPassword.Text;
            if(checkLogin(userName, passWord))
            {
                Client c = new Client();
                this.Hide();
                c.Show();
                c.LogOut += C_LogOut;                          
            }
            else
            {
                MessageBox.Show("Sai ten tai khoan mat khau", "Loi", MessageBoxButtons.OK);
                txtUsername.Focus();
                return;
            }
        }

        private void C_LogOut(object sender, EventArgs e)
        {
            (sender as Client).isExit = false;
            (sender as Client).Close();
            this.Show();
        }

        private void LogIn_FormClosed(object sender, FormClosedEventArgs e)
        {
            Application.Exit();
        }

        private void LogIn_FormClosing(object sender, FormClosingEventArgs e)
        {        
                if (MessageBox.Show("Thoat chuong trinh", "canh bao", MessageBoxButtons.YesNo) != DialogResult.Yes)
                    e.Cancel = true;           
        }

        bool checkLogin(string userName, string passWord)
        {

            for(int i=0; i<ListUser.Instance.ListAccountUser.Count;i++)
            {
                if (userName == ListUser.Instance.ListAccountUser[i].UserName && passWord == ListUser.Instance.ListAccountUser[i].PassWord)
                    return true;
            }
            return false;
        }
    }
}
