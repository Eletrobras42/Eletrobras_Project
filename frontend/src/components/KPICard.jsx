import { TrendingUp, Zap, AlertTriangle, Target, Activity, BarChart3 } from 'lucide-react';

function KPICard({ title, value, icon: Icon, color = "blue", trend }) {
  const colorClasses = {
    blue: "text-accent-blue",
    green: "text-accent-green",
    orange: "text-accent-orange",
    red: "text-accent-red",
    purple: "text-accent-purple"
  };

  return (
    <div className="kpi-card">
      <div className="flex items-center justify-between mb-4">
        <div className={`p-3 rounded-lg bg-dark-bg ${colorClasses[color]}`}>
          <Icon size={24} />
        </div>
        {trend && (
          <div className="flex items-center text-sm">
            <TrendingUp size={16} className="mr-1" />
            <span className={trend > 0 ? "text-accent-green" : "text-accent-red"}>
              {trend > 0 ? "+" : ""}{trend}%
            </span>
          </div>
        )}
      </div>
      <div className="kpi-value">{value}</div>
      <div className="kpi-label">{title}</div>
    </div>
  );
}

export default KPICard;